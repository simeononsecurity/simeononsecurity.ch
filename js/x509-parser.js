/*
 * Minimal X.509 and ASN.1 DER reader for the certificate tools.
 *
 * Runs entirely in the browser. No network access, no dependencies.
 * Deliberately small: it understands the parts of RFC 5280 the two tools need
 * and throws a readable error on anything it cannot decode, rather than
 * guessing.
 */
var X509 = (function () {
  'use strict';

  /* ---------------------------------------------------------------- DER ---- */

  function readLength(bytes, pos) {
    var first = bytes[pos];
    if (first === undefined) { throw new Error('Unexpected end of DER data'); }
    if ((first & 0x80) === 0) { return { length: first, size: 1 }; }
    var count = first & 0x7f;
    if (count === 0) { throw new Error('Indefinite length is not valid DER'); }
    if (count > 4) { throw new Error('Length field is too large to represent safely'); }
    var length = 0;
    for (var i = 0; i < count; i++) { length = (length * 256) + bytes[pos + 1 + i]; }
    return { length: length, size: 1 + count };
  }

  function element(bytes, pos, end) {
    if (end === undefined) { end = bytes.length; }
    if (pos >= end) { throw new Error('Unexpected end of DER data'); }
    var tag = bytes[pos];
    var number = tag & 0x1f;
    if (number === 0x1f) { throw new Error('High tag numbers are not supported'); }
    var length = readLength(bytes, pos + 1);
    var valueStart = pos + 1 + length.size;
    var valueEnd = valueStart + length.length;
    if (valueEnd > end) { throw new Error('DER element runs past the end of its parent'); }
    return {
      tag: tag,
      cls: tag >> 6,
      constructed: (tag & 0x20) !== 0,
      number: number,
      start: pos,
      valueStart: valueStart,
      valueEnd: valueEnd,
      next: valueEnd
    };
  }

  function children(bytes, seq) {
    var out = [];
    var pos = seq.valueStart;
    while (pos < seq.valueEnd) {
      var el = element(bytes, pos, seq.valueEnd);
      out.push(el);
      pos = el.next;
    }
    return out;
  }

  function isContext(el, number) {
    return el.cls === 2 && el.number === number;
  }

  function toBytes(bytes, el) {
    return bytes.slice(el.valueStart, el.valueEnd);
  }

  function toInt(bytes, el) {
    var value = 0;
    for (var i = el.valueStart; i < el.valueEnd; i++) { value = (value * 256) + bytes[i]; }
    return value;
  }

  function toHex(bytes, el) {
    var out = '';
    for (var i = el.valueStart; i < el.valueEnd; i++) {
      out += ('0' + bytes[i].toString(16)).slice(-2);
    }
    return out;
  }

  function toOid(bytes, el) {
    if (el.valueEnd <= el.valueStart) { return ''; }
    var first = bytes[el.valueStart];
    var parts = [Math.floor(first / 40), first % 40];
    var value = 0;
    var pending = false;
    for (var i = el.valueStart + 1; i < el.valueEnd; i++) {
      var b = bytes[i];
      value = (value * 128) + (b & 0x7f);
      pending = true;
      if ((b & 0x80) === 0) { parts.push(value); value = 0; pending = false; }
    }
    if (pending) { throw new Error('Truncated object identifier'); }
    return parts.join('.');
  }

  function toText(bytes, el) {
    var slice = bytes.slice(el.valueStart, el.valueEnd);
    if (el.number === 0x1e) {
      // BMPString is UTF-16 big endian.
      var out = '';
      for (var i = 0; i + 1 < slice.length; i += 2) {
        out += String.fromCharCode((slice[i] << 8) | slice[i + 1]);
      }
      return out;
    }
    try {
      return new TextDecoder('utf-8', { fatal: false }).decode(slice);
    } catch (error) {
      var raw = '';
      for (var j = 0; j < slice.length; j++) { raw += String.fromCharCode(slice[j]); }
      return raw;
    }
  }

  function toTime(bytes, el) {
    var text = toText(bytes, el);
    var match = text.match(/^(\d{2}|\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})?(?:Z|[+-]\d{4})?$/);
    if (!match) { throw new Error('Unrecognised time value: ' + text); }
    var year = parseInt(match[1], 10);
    if (match[1].length === 2) {
      // UTCTime pivots at 1950, per RFC 5280.
      year = year >= 50 ? 1900 + year : 2000 + year;
    }
    return new Date(Date.UTC(
      year,
      parseInt(match[2], 10) - 1,
      parseInt(match[3], 10),
      parseInt(match[4], 10),
      parseInt(match[5], 10),
      match[6] ? parseInt(match[6], 10) : 0
    ));
  }

  function toBitString(bytes, el) {
    // The first content byte is the count of unused trailing bits.
    if (el.valueEnd <= el.valueStart) { return { unused: 0, bytes: new Uint8Array(0) }; }
    return {
      unused: bytes[el.valueStart],
      bytes: bytes.slice(el.valueStart + 1, el.valueEnd)
    };
  }

  function toBase64(bytes) {
    var binary = '';
    for (var i = 0; i < bytes.length; i++) { binary += String.fromCharCode(bytes[i]); }
    return btoa(binary);
  }

  /* -------------------------------------------------------------- tables ---- */

  var NAME_OIDS = {
    '2.5.4.3': 'CN',
    '2.5.4.4': 'SN',
    '2.5.4.5': 'serialNumber',
    '2.5.4.6': 'C',
    '2.5.4.7': 'L',
    '2.5.4.8': 'ST',
    '2.5.4.9': 'street',
    '2.5.4.10': 'O',
    '2.5.4.11': 'OU',
    '2.5.4.12': 'title',
    '2.5.4.42': 'givenName',
    '0.9.2342.19200300.100.1.25': 'DC',
    '1.2.840.113549.1.9.1': 'emailAddress'
  };

  var SIG_ALGORITHMS = {
    '1.2.840.113549.1.1.5': { name: 'SHA-1 with RSA', hash: 'SHA-1', family: 'RSA', weak: true },
    '1.2.840.113549.1.1.11': { name: 'SHA-256 with RSA', hash: 'SHA-256', family: 'RSA' },
    '1.2.840.113549.1.1.12': { name: 'SHA-384 with RSA', hash: 'SHA-384', family: 'RSA' },
    '1.2.840.113549.1.1.13': { name: 'SHA-512 with RSA', hash: 'SHA-512', family: 'RSA' },
    '1.2.840.113549.1.1.10': { name: 'RSA-PSS', hash: 'SHA-256', family: 'PSS' },
    '1.2.840.10045.4.1': { name: 'SHA-1 with ECDSA', hash: 'SHA-1', family: 'ECDSA', weak: true },
    '1.2.840.10045.4.3.2': { name: 'SHA-256 with ECDSA', hash: 'SHA-256', family: 'ECDSA' },
    '1.2.840.10045.4.3.3': { name: 'SHA-384 with ECDSA', hash: 'SHA-384', family: 'ECDSA' },
    '1.2.840.10045.4.3.4': { name: 'SHA-512 with ECDSA', hash: 'SHA-512', family: 'ECDSA' },
    '1.3.101.112': { name: 'Ed25519', hash: null, family: 'Ed25519' }
  };

  var KEY_ALGORITHMS = {
    '1.2.840.113549.1.1.1': 'RSA',
    '1.2.840.113549.1.1.10': 'RSA-PSS',
    '1.2.840.10045.2.1': 'EC',
    '1.3.101.112': 'Ed25519',
    '1.2.840.10040.4.1': 'DSA'
  };

  var EC_CURVES = {
    '1.2.840.10045.3.1.7': { name: 'P-256', size: 32 },
    '1.3.132.0.34': { name: 'P-384', size: 48 },
    '1.3.132.0.35': { name: 'P-521', size: 66 }
  };

  var EXTENSIONS = {
    '2.5.29.14': 'Subject Key Identifier',
    '2.5.29.15': 'Key Usage',
    '2.5.29.17': 'Subject Alternative Name',
    '2.5.29.18': 'Issuer Alternative Name',
    '2.5.29.19': 'Basic Constraints',
    '2.5.29.30': 'Name Constraints',
    '2.5.29.31': 'CRL Distribution Points',
    '2.5.29.32': 'Certificate Policies',
    '2.5.29.33': 'Policy Mappings',
    '2.5.29.35': 'Authority Key Identifier',
    '2.5.29.36': 'Policy Constraints',
    '2.5.29.37': 'Extended Key Usage',
    '2.5.29.54': 'Inhibit Any Policy',
    '1.3.6.1.5.5.7.1.1': 'Authority Information Access',
    '1.3.6.1.5.5.7.1.11': 'Subject Information Access',
    '1.3.6.1.5.5.7.1.24': 'TLS Feature',
    '1.3.6.1.4.1.11129.2.4.2': 'Certificate Transparency SCT list'
  };

  var EKU_NAMES = {
    '1.3.6.1.5.5.7.3.1': 'TLS server authentication',
    '1.3.6.1.5.5.7.3.2': 'TLS client authentication',
    '1.3.6.1.5.5.7.3.3': 'Code signing',
    '1.3.6.1.5.5.7.3.4': 'Email protection',
    '1.3.6.1.5.5.7.3.8': 'Time stamping',
    '1.3.6.1.5.5.7.3.9': 'OCSP signing',
    '2.5.29.37.0': 'Any extended key usage'
  };

  var KEY_USAGE_BITS = [
    'digitalSignature', 'nonRepudiation', 'keyEncipherment', 'dataEncipherment',
    'keyAgreement', 'keyCertSign', 'cRLSign', 'encipherOnly', 'decipherOnly'
  ];

  /* -------------------------------------------------------------- input ---- */

  function base64ToBytes(text) {
    var padded = text.replace(/[^A-Za-z0-9+/=]/g, '');
    var binary = atob(padded);
    var bytes = new Uint8Array(binary.length);
    for (var i = 0; i < binary.length; i++) { bytes[i] = binary.charCodeAt(i); }
    return bytes;
  }

  function looksLikeDer(bytes) {
    // A certificate is a SEQUENCE, so the first byte is 0x30.
    return bytes.length > 8 && bytes[0] === 0x30;
  }

  /*
   * Accepts a PEM bundle containing several blocks, a single PEM block, bare
   * base64, or a pasted DER blob that survived being read as text. Returns one
   * entry per certificate, with an error field instead of throwing so a bundle
   * with one bad block still yields the rest.
   */
  function readCertificates(text) {
    var out = [];
    var pattern = /-----BEGIN\s+([A-Z0-9 ]+)-----\s*([\s\S]*?)-----END\s+\1-----/g;
    var match;
    while ((match = pattern.exec(text)) !== null) {
      var body = match[2].replace(/\s+/g, '');
      if (!body) { continue; }
      try {
        out.push({ der: base64ToBytes(body), label: match[1].trim() });
      } catch (error) {
        out.push({ error: 'A PEM block labelled ' + match[1].trim() + ' is not valid base64.' });
      }
    }
    if (out.length) { return out; }

    var bare = text.replace(/\s+/g, '');
    if (bare.length > 100 && /^[A-Za-z0-9+/=]+$/.test(bare)) {
      try {
        var decoded = base64ToBytes(bare);
        if (looksLikeDer(decoded)) { return [{ der: decoded, label: 'base64 decoded' }]; }
      } catch (error) { /* fall through to the raw case */ }
    }

    var raw = new Uint8Array(text.length);
    for (var i = 0; i < text.length; i++) { raw[i] = text.charCodeAt(i) & 0xff; }
    if (looksLikeDer(raw)) { return [{ der: raw, label: 'raw DER' }]; }
    return [];
  }

  /* --------------------------------------------------------------- names ---- */

  function parseName(bytes, seq) {
    var rdns = [];
    children(bytes, seq).forEach(function (set) {
      children(bytes, set).forEach(function (pair) {
        var parts = children(bytes, pair);
        if (parts.length < 2) { return; }
        var oid = toOid(bytes, parts[0]);
        var value;
        try {
          value = toText(bytes, parts[1]);
        } catch (error) {
          value = toHex(bytes, parts[1]);
        }
        rdns.push({ oid: oid, short: NAME_OIDS[oid] || oid, value: value });
      });
    });
    return rdns;
  }

  function formatName(rdns) {
    if (!rdns || !rdns.length) { return '(empty)'; }
    return rdns.map(function (rdn) { return rdn.short + '=' + rdn.value; }).join(', ');
  }

  function nameKey(rdns) {
    // A stable string for matching issuers to subjects.
    return rdns.map(function (rdn) { return rdn.oid + '=' + rdn.value; }).join('|');
  }

  /* ---------------------------------------------------------- extensions ---- */

  function generalNameValue(bytes, el) {
    var tag = el.cls === 2 ? el.number : el.tag;
    if (tag === 7 && (el.valueEnd - el.valueStart) === 4) {
      return bytes[el.valueStart] + '.' + bytes[el.valueStart + 1] + '.' +
        bytes[el.valueStart + 2] + '.' + bytes[el.valueStart + 3];
    }
    if (tag === 4) {
      try { return formatName(parseName(bytes, el)); } catch (error) { return '(directory name)'; }
    }
    if (tag === 1 || tag === 2 || tag === 6) {
      try { return toText(bytes, el); } catch (error) { return toHex(bytes, el); }
    }
    return toHex(bytes, el);
  }

  function decodeGeneralNames(bytes, seq) {
    return children(bytes, seq).map(function (el) {
      return { tag: el.cls === 2 ? el.number : el.tag, value: generalNameValue(bytes, el) };
    });
  }

  function collectUris(bytes, el) {
    var out = [];
    (function walk(node) {
      if (node.cls === 2 && node.number === 6) {
        out.push(toText(bytes, node));
        return;
      }
      if (node.constructed) { children(bytes, node).forEach(walk); }
    })(el);
    return out;
  }

  function colonHex(bytes) {
    var parts = [];
    for (var i = 0; i < bytes.length; i++) {
      parts.push(('0' + bytes[i].toString(16)).slice(-2).toUpperCase());
    }
    return parts.join(':');
  }

  function summarizeExtension(oid, value) {
    var top = element(value, 0, value.length);
    var inner = children(value, top);

    if (oid === '2.5.29.15') {
      var bits = toBitString(value, top);
      var names = [];
      for (var i = 0; i < KEY_USAGE_BITS.length; i++) {
        if (bits.bytes[i >> 3] & (0x80 >> (i & 7))) { names.push(KEY_USAGE_BITS[i]); }
      }
      return names.length ? names.join(', ') : 'none set';
    }

    if (oid === '2.5.29.17' || oid === '2.5.29.18') {
      var names2 = decodeGeneralNames(value, top);
      var labels = { 1: 'email', 2: 'DNS', 6: 'URI', 7: 'IP', 8: 'registered ID' };
      return names2.map(function (n) {
        return (labels[n.tag] || ('tag ' + n.tag)) + ':' + n.value;
      }).join('\n');
    }

    if (oid === '2.5.29.19') {
      var ca = false;
      var pathLen = null;
      inner.forEach(function (el) {
        if (el.tag === 0x01) { ca = value[el.valueStart] !== 0; }
        if (el.tag === 0x02) { pathLen = toInt(value, el); }
      });
      return 'CA:' + (ca ? 'TRUE' : 'FALSE') + (pathLen === null ? '' : ', path length ' + pathLen);
    }

    if (oid === '2.5.29.37') {
      return inner.map(function (el) {
        var ekuOid = toOid(value, el);
        return EKU_NAMES[ekuOid] || ekuOid;
      }).join(', ');
    }

    if (oid === '2.5.29.14') {
      return colonHex(toBytes(value, top));
    }

    if (oid === '2.5.29.35') {
      var found = null;
      inner.forEach(function (el) {
        if (el.cls === 2 && el.number === 0) { found = colonHex(toBytes(value, el)); }
      });
      return found || '(not present)';
    }

    if (oid === '2.5.29.31' || oid === '1.3.6.1.5.5.7.1.1') {
      var uris = collectUris(value, top);
      return uris.length ? uris.join('\n') : '(no URIs found)';
    }

    if (oid === '2.5.29.32') {
      return children(value, top).map(function (policy) {
        var policyParts = children(value, policy);
        return toOid(value, policyParts[0]);
      }).join(', ');
    }

    if (oid === '1.3.6.1.4.1.11129.2.4.2') {
      // The SCT list is an opaque blob, so only its size is meaningful here.
      var octets = top.tag === 0x04 ? toBytes(value, top) : toBytes(value, top);
      return 'present, ' + octets.length + ' bytes of signed certificate timestamps';
    }

    if (oid === '1.3.6.1.5.5.7.1.24') {
      var features = inner.map(function (el) { return toInt(value, el); });
      var described = features.map(function (f) {
        if (f === 5) { return 'status_request (OCSP must-staple)'; }
        if (f === 17) { return 'status_request_v2'; }
        return 'feature ' + f;
      });
      return described.join(', ');
    }

    return toHex(value, top).slice(0, 120) + (top.valueEnd - top.valueStart > 60 ? '...' : '');
  }

  function parseExtensions(bytes, wrapper) {
    var list = [];
    var byOid = {};

    // The caller hands over the [3] EXPLICIT wrapper, whose single child is the
    // SEQUENCE OF Extension. Descend one level when the wrapper is present, so
    // this also works if a plain SEQUENCE is passed in.
    var seq = wrapper;
    if (wrapper.cls === 2) {
      var wrapped = children(bytes, wrapper);
      if (!wrapped.length) { return { list: list, byOid: byOid }; }
      seq = wrapped[0];
    }

    children(bytes, seq).forEach(function (extEl) {
      var parts = children(bytes, extEl);
      if (parts.length < 2) { return; }
      var oid = toOid(bytes, parts[0]);
      var index = 1;
      var critical = false;
      if (parts[index].tag === 0x01) { critical = bytes[parts[index].valueStart] !== 0; index++; }
      var rawValue = toBytes(bytes, parts[index]);
      var ext = { oid: oid, name: EXTENSIONS[oid] || oid, critical: critical, summary: '', rawValue: rawValue };
      try {
        ext.summary = summarizeExtension(oid, rawValue);
      } catch (error) {
        ext.summary = 'could not be decoded: ' + error.message;
      }
      list.push(ext);
      byOid[oid] = ext;
    });
    return { list: list, byOid: byOid };
  }

  /* --------------------------------------------------------- certificate ---- */

  function integerBits(bytes, el) {
    var start = el.valueStart;
    while (start < el.valueEnd && bytes[start] === 0) { start++; }
    if (start >= el.valueEnd) { return 0; }
    var bits = (el.valueEnd - start) * 8;
    var top = bytes[start];
    while (top > 0 && (top & 0x80) === 0) { bits--; top = (top << 1) & 0xff; }
    return bits;
  }

  function decodeKeyUsage(raw) {
    var out = [];
    try {
      var bits = toBitString(raw, element(raw, 0, raw.length));
      for (var i = 0; i < KEY_USAGE_BITS.length; i++) {
        if (bits.bytes[i >> 3] & (0x80 >> (i & 7))) { out.push(KEY_USAGE_BITS[i]); }
      }
    } catch (error) { /* leave the list empty */ }
    return out;
  }

  function decodeBasicConstraints(raw) {
    var result = { ca: false, pathLen: null };
    try {
      var top = element(raw, 0, raw.length);
      children(raw, top).forEach(function (el) {
        if (el.tag === 0x01) { result.ca = raw[el.valueStart] !== 0; }
        if (el.tag === 0x02) { result.pathLen = toInt(raw, el); }
      });
    } catch (error) { /* leave the defaults */ }
    return result;
  }

  function parseCertificate(der) {
    var top = element(der, 0, der.length);
    var outer = children(der, top);
    if (outer.length < 3) {
      throw new Error('A certificate needs a body, a signature algorithm and a signature value');
    }

    var tbs = outer[0];
    var signatureOid = toOid(der, children(der, outer[1])[0]);
    var signatureAlg = SIG_ALGORITHMS[signatureOid] || { name: signatureOid, hash: null, family: 'unknown' };
    var signatureBytes = toBitString(der, outer[2]).bytes;

    var body = children(der, tbs);
    var index = 0;
    var version = 1;
    if (isContext(body[0], 0)) {
      version = toInt(der, children(der, body[0])[0]) + 1;
      index = 1;
    }

    var serial = toHex(der, body[index++]);
    index++; // the inner algorithm identifier repeats the outer one
    var issuer = parseName(der, body[index++]);
    var validity = children(der, body[index++]);
    var subject = parseName(der, body[index++]);
    var spki = body[index++];

    var extensions = { list: [], byOid: {} };
    for (var i = index; i < body.length; i++) {
      if (isContext(body[i], 3)) { extensions = parseExtensions(der, body[i]); }
    }

    var spkiParts = children(der, spki);
    var keyAlgParts = children(der, spkiParts[0]);
    var keyAlg = KEY_ALGORITHMS[toOid(der, keyAlgParts[0])] || toOid(der, keyAlgParts[0]);
    // Web Crypto needs the complete DER element, header included, not the
    // content of the sequence.
    var spkiBytes = der.slice(spki.start, spki.next);

    var curveName = '';
    var curveSize = 0;
    var keyBits = 0;

    if (keyAlg === 'EC' && keyAlgParts.length > 1) {
      var curveOid = toOid(der, keyAlgParts[1]);
      if (EC_CURVES[curveOid]) {
        curveName = EC_CURVES[curveOid].name;
        curveSize = EC_CURVES[curveOid].size;
        keyBits = curveSize * 8;
      } else {
        curveName = curveOid;
      }
    } else if (keyAlg === 'Ed25519') {
      keyBits = 256;
    } else if (keyAlg === 'RSA' || keyAlg === 'RSA-PSS') {
      try {
        var rsaBytes = toBitString(der, spkiParts[1]).bytes;
        var rsaTop = element(rsaBytes, 0, rsaBytes.length);
        keyBits = integerBits(rsaBytes, children(rsaBytes, rsaTop)[0]);
      } catch (error) { keyBits = 0; }
    }

    var sanAll = [];
    var sanDns = [];
    var sanExt = extensions.byOid['2.5.29.17'];
    if (sanExt && sanExt.rawValue) {
      try {
        sanAll = decodeGeneralNames(sanExt.rawValue, element(sanExt.rawValue, 0, sanExt.rawValue.length));
        sanAll.forEach(function (name) {
          if (name.tag === 2) { sanDns.push(name.value.toLowerCase()); }
        });
      } catch (error) { /* leave the SAN list empty */ }
    }

    var bcExt = extensions.byOid['2.5.29.19'];
    var basic = bcExt && bcExt.rawValue ? decodeBasicConstraints(bcExt.rawValue) : { ca: false, pathLen: null };
    var kuExt = extensions.byOid['2.5.29.15'];
    var keyUsage = kuExt && kuExt.rawValue ? decodeKeyUsage(kuExt.rawValue) : [];

    var subjectKey = nameKey(subject);

    return {
      der: der,
      version: version,
      serial: serial,
      subject: subject,
      subjectText: formatName(subject),
      issuer: issuer,
      issuerText: formatName(issuer),
      notBefore: toTime(der, validity[0]),
      notAfter: toTime(der, validity[1]),
      signatureOid: signatureOid,
      signatureAlg: signatureAlg,
      signatureBytes: signatureBytes,
      tbsBytes: der.slice(tbs.start, tbs.next),
      spkiBytes: spkiBytes,
      keyAlg: keyAlg,
      keyBits: keyBits,
      curveName: curveName,
      curveSize: curveSize,
      extensions: extensions,
      sanAll: sanAll,
      sanDns: sanDns,
      isCa: basic.ca,
      pathLen: basic.pathLen,
      keyUsage: keyUsage,
      subjectKey: subjectKey,
      isSelfSigned: subjectKey !== '' && subjectKey === nameKey(issuer)
    };
  }

  async function fingerprints(der) {
    if (!window.crypto || !window.crypto.subtle) { return null; }
    var sha256 = new Uint8Array(await crypto.subtle.digest('SHA-256', der));
    var sha1 = new Uint8Array(await crypto.subtle.digest('SHA-1', der));
    return { sha256: colonHex(sha256), sha1: colonHex(sha1) };
  }

  // X.509 stores ECDSA signatures as a DER SEQUENCE of two INTEGERs, while Web
  // Crypto expects the raw r||s pair, so both integers are re-padded to the
  // curve size before verification.
  function ecdsaDerToRaw(signature, size) {
    var out = new Uint8Array(size * 2);
    var bad = false;
    try {
      var parts = children(signature, element(signature, 0, signature.length));
      if (parts.length !== 2) { return null; }
      [parts[0], parts[1]].forEach(function (el, index) {
        var start = el.valueStart;
        while (start < el.valueEnd && signature[start] === 0) { start++; }
        var length = el.valueEnd - start;
        if (length > size) { bad = true; return; }
        out.set(signature.slice(start, el.valueEnd), index * size + (size - length));
      });
    } catch (error) {
      return null;
    }
    return bad ? null : out;
  }

  async function verifySignature(child, parent) {
    var alg = SIG_ALGORITHMS[child.signatureOid];
    if (!alg) {
      return { ok: false, skipped: true, reason: 'No verifier for signature algorithm ' + child.signatureOid };
    }
    if (!window.crypto || !window.crypto.subtle) {
      return { ok: false, skipped: true, reason: 'Web Crypto is unavailable, which needs a secure context over HTTPS' };
    }

    try {
      if (alg.family === 'RSA' || alg.family === 'PSS') {
        var isPss = alg.family === 'PSS';
        var importParams = isPss
          ? { name: 'RSA-PSS', hash: alg.hash }
          : { name: 'RSASSA-PKCS1-v1_5', hash: alg.hash };
        var verifyParams = isPss ? { name: 'RSA-PSS', saltLength: 32 } : { name: 'RSASSA-PKCS1-v1_5' };
        var rsaKey = await crypto.subtle.importKey('spki', parent.spkiBytes, importParams, false, ['verify']);
        var rsaOk = await crypto.subtle.verify(verifyParams, rsaKey, child.signatureBytes, child.tbsBytes);
        return { ok: rsaOk, reason: rsaOk ? '' : 'The signature does not match the issuer public key' };
      }

      if (alg.family === 'ECDSA') {
        if (!parent.curveName) {
          return { ok: false, skipped: true, reason: 'The issuer curve is not one this tool recognises' };
        }
        var ecKey = await crypto.subtle.importKey(
          'spki', parent.spkiBytes, { name: 'ECDSA', namedCurve: parent.curveName }, false, ['verify']
        );
        var raw = ecdsaDerToRaw(child.signatureBytes, parent.curveSize);
        if (!raw) {
          return { ok: false, skipped: true, reason: 'The DER ECDSA signature could not be converted to raw r and s' };
        }
        var ecOk = await crypto.subtle.verify({ name: 'ECDSA', hash: alg.hash }, ecKey, raw, child.tbsBytes);
        return { ok: ecOk, reason: ecOk ? '' : 'The signature does not match the issuer public key' };
      }

      if (alg.family === 'Ed25519') {
        try {
          var edKey = await crypto.subtle.importKey('spki', parent.spkiBytes, { name: 'Ed25519' }, false, ['verify']);
          var edOk = await crypto.subtle.verify({ name: 'Ed25519' }, edKey, child.signatureBytes, child.tbsBytes);
          return { ok: edOk, reason: edOk ? '' : 'The signature does not match the issuer public key' };
        } catch (error) {
          return { ok: false, skipped: true, reason: 'This browser cannot verify Ed25519 through Web Crypto' };
        }
      }

      return { ok: false, skipped: true, reason: 'No verifier available for the ' + alg.family + ' family' };
    } catch (error) {
      return { ok: false, skipped: true, reason: 'Verification could not run: ' + error.message };
    }
  }

  function hostnameMatches(cert, hostname) {
    var host = String(hostname || '').trim().toLowerCase().replace(/\.$/, '');
    if (!host) { return { checked: false, matched: false, reason: 'No hostname was supplied.' }; }

    var isIpv4 = /^\d{1,3}(\.\d{1,3}){3}$/.test(host);
    var names = [];
    var source = 'subjectAltName';

    cert.sanAll.forEach(function (name) {
      if (isIpv4 && name.tag === 7) { names.push(name.value); }
      if (!isIpv4 && name.tag === 2) { names.push(name.value.toLowerCase()); }
    });

    if (!names.length && !isIpv4) {
      // Common name is a fallback only, since browsers stopped accepting it.
      cert.subject.forEach(function (rdn) {
        if (rdn.short === 'CN') { names.push(rdn.value.toLowerCase()); }
      });
      source = 'commonName, which browsers no longer accept as a fallback';
    }

    if (!names.length) {
      return { checked: true, matched: false, reason: 'The certificate lists no name of the type being checked.', names: [] };
    }

    for (var i = 0; i < names.length; i++) {
      var pattern = names[i];
      if (pattern === host) {
        return { checked: true, matched: true, matchedName: pattern, source: source, names: names };
      }
      if (pattern.charAt(0) === '*') {
        // A wildcard covers exactly one label and never the bare domain, so
        // *.example.com matches a.example.com but not a.b.example.com.
        var suffix = pattern.substring(1);
        if (host.length > suffix.length && host.slice(-suffix.length) === suffix) {
          var prefix = host.slice(0, host.length - suffix.length);
          if (prefix.length > 0 && prefix.indexOf('.') === -1) {
            return { checked: true, matched: true, matchedName: pattern, source: source, names: names };
          }
        }
      }
    }
    return { checked: true, matched: false, reason: 'No listed name matches.', names: names };
  }

  return {
    element: element,
    children: children,
    isContext: isContext,
    toBytes: toBytes,
    toInt: toInt,
    toHex: toHex,
    toOid: toOid,
    toText: toText,
    toTime: toTime,
    toBitString: toBitString,
    toBase64: toBase64,
    colonHex: colonHex,
    readCertificates: readCertificates,
    parseName: parseName,
    formatName: formatName,
    nameKey: nameKey,
    parseExtensions: parseExtensions,
    parseCertificate: parseCertificate,
    fingerprints: fingerprints,
    verifySignature: verifySignature,
    hostnameMatches: hostnameMatches,
    NAME_OIDS: NAME_OIDS,
    SIG_ALGORITHMS: SIG_ALGORITHMS,
    KEY_ALGORITHMS: KEY_ALGORITHMS,
    EC_CURVES: EC_CURVES,
    EXTENSIONS: EXTENSIONS,
    EKU_NAMES: EKU_NAMES,
    KEY_USAGE_BITS: KEY_USAGE_BITS
  };
})();




