---
title: "Module 8: Open-Source Intelligence"
date: 2026-09-12
lastmod: 2026-09-17
toc: true
draft: false
description: "Evaluate public sources, RDAP, DNS, certificate logs, and scan data. Build a traceable OSINT brief with worked examples and source-quality checks."
genre: ["Red Team", "Offensive Security", "OSINT"]
tags: ["red team", "OSINT", "Google dorks", "Whois", "Shodan", "SpiderFoot", "theHarvester", "Maltego", "subdomain enumeration", "certificate transparency", "crt.sh", "GEOINT", "ADS-B", "AIS", "open source intelligence", "red team course"]
cover: "/img/cover/open-source-intelligence-osint-collection-techniques.webp"
coverAlt: "A modern workspace with multiple screens showing open-source intelligence data, including social media feeds and analytics, against a dark background. Abstract data flows connect the screens."
coverCaption: "Module 8: turn public observations into supported decisions."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Open-source intelligence (OSINT)** turns publicly available information into an answer to a defined question. Collection alone produces observations. Useful intelligence adds provenance, context, corroboration, uncertainty, and a decision the assessment team is authorized to make.

*Allow about 25 minutes, plus time to complete the evidence-ledger exercise. All organizations, observations, and assessment decisions in the worked case are fictional.*

## What You Will Learn

- **Distinguish** a source observation from an inference and a confirmed finding.
- **Explain** the limits of registration, DNS, certificate, and scan-index data.
- **Apply** search operators and normalize a synthetic list of names.
- **Compare** evidence freshness and independent corroboration.
- **Create** a research brief which supports a bounded next action.

| Term | Meaning |
|---|---|
| **Provenance** | Where information originated and how you obtained it |
| **Observation** | A specific item recorded from a source |
| **Inference** | A conclusion drawn from one or more observations |
| **Corroboration** | Additional evidence supporting or challenging a claim |
| **RDAP** | Registration Data Access Protocol for structured registration queries |
| **Certificate transparency** | Public logging system for certificates and precertificates |
| **ASN** | Autonomous system number identifying a routing administration |

## Start With a Question

**A research question** limits both collection and interpretation. “Which externally named services need ownership clarification before our approved scan?” produces a different collection plan from “Which public documents describe the organization's remote-work policy?” Write the question before opening tools.

**A finding** needs a supported statement and its boundary. A search result mentioning a product does not prove the product is deployed now. A service banner naming a version does not establish the installed patch state or exploitability.

**Decision relevance** keeps the work focused. If a source does not change the answer or the next authorized action, collecting more of it adds handling work without improving the result. Maintain a short list of unresolved questions instead of an unlimited list of names.

| Research question | Useful evidence | Premature conclusion |
|---|---|---|
| **Who manages a service?** | Current inventory plus registration context | Shared IP means shared ownership |
| **Was a name publicly disclosed?** | Dated certificate or document record | The service is live today |
| **Is a technology plausible?** | Recent technical publication | Every listed product is deployed |

## Map the Collection Path

**Public availability** describes access to information, not the visibility of collecting it. Reading a search index, loading the original website, and requesting a fresh service banner contact different systems. Search providers, APIs, resolvers, and websites have their own records of activity.

**Passive relative to the target** is a useful description if you define it. Querying an existing third-party dataset often avoids a new connection from you to the target service. Opening a result, fetching a linked image, or enabling an active tool module changes the collection path.

**Collection records** should therefore name the provider, account context where applicable, query, timestamp, and whether the tool initiates fresh target contact. An isolated browser profile separates work from personal sessions, but it does not guarantee anonymity or eliminate service-side logs.

{{< figure src="osint-observation-to-decision.webp" alt="Four connected boxes move from a research question to source observations, corroboration, and a bounded decision with uncertainty recorded" caption="Public information becomes useful intelligence through supported interpretation" >}}

## Use Search Operators Deliberately

**Search operators** narrow indexed results. Google documents quoted phrases, **`site:`**, **`filetype:`**, exclusions with **`-`**, and date filters such as **`after:`**. Operator support and interpretation differ between services, so check the search engine's documentation. [Read Google's search guidance](https://support.google.com/websearch/answer/2466433?hl=en).

**Practice query design** with the fictional examples below. The reserved example domain is a placeholder, so no matching results are expected. Replace it only with the domain selected for your authorized research task. [Read IANA's example-domain guidance](https://www.iana.org/help/example-domains).

```text
site:example.com "remote access"
site:example.com filetype:pdf "annual report"
site:example.com "service status" -careers
site:example.com "migration" after:2025-01-01
```

**Explain each filter** before collecting results. The first limits the site and requests an exact phrase, the second adds a document type, the third excludes a word, and the fourth applies a date condition. A search-engine date filter is a retrieval aid, so verify the source's own dates before interpreting freshness.

**An empty result set** is limited evidence. Indexing gaps, query wording, access restrictions, and removed pages affect the result. Record the query and its limits instead of concluding the organization has no remote-access service.

| Source item | Preserve | Avoid assuming |
|---|---|---|
| **Search snippet** | Query, retrieval time, and destination | Snippet equals current page content |
| **Public document** | Original file, date, and source URL | Metadata proves current employment |
| **Job posting** | Publication context and named requirements | Every listed skill reflects production use |

## Read Registration Records Carefully

**Domain registration data** and **IP-number registration data** answer different questions. ICANN's January 2025 transition made RDAP the definitive delivery mechanism for generic top-level-domain registration information in place of sunsetted WHOIS requirements. This does not mean every country-code domain or number-registry service follows an identical transition. [Read ICANN's announcement](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en).

**Regional Internet Registries** provide number-resource information. ARIN's RDAP documentation covers queries for networks, autonomous systems, and related entities. A returned record describes registration relationships, not necessarily the current application operator using an address. [Read ARIN's RDAP guide](https://www.arin.net/resources/registry/whois/rdap/).

**Scope remains a separate record.** A cloud provider's allocation does not authorize testing every tenant within it. Conversely, a customer-operated service on provider address space is not automatically excluded if the agreed scope and applicable provider conditions explicitly include it.

| Record | Supports | Does not establish |
|---|---|---|
| **Domain RDAP** | Registration details exposed by the service | Current technical administrator in every case |
| **Network RDAP** | Number-resource registration context | Application ownership or assessment permission |
| **Approved asset register** | Named assessment targets and constraints | Current network state without verification |

## Interpret DNS Relationships

**DNS names** are not a one-to-one inventory of machines. Multiple names resolve to one service, one name resolves to multiple addresses, and an alias refers to another name. Delegation also separates a parent zone from a child zone. [Read the DNS concepts specification](https://www.rfc-editor.org/rfc/rfc1034.html).

**Record types** provide different evidence. Address records associate names with addresses, MX records identify mail exchangers, NS records describe authoritative servers, and TXT records carry text with application-specific meaning. A TXT value mentioning a provider is a lead about configuration, not proof every provider feature is active.

**AXFR** transfers the contents of a DNS zone under the protocol's rules. It is not inherently a misconfiguration and does not return every host in an entire delegated domain tree. Whether a requester is permitted to receive a zone is an authorization and configuration question. [Read the AXFR specification](https://www.rfc-editor.org/rfc/rfc5936.html).

| Observation | Reasonable interpretation |
|---|---|
| **Two names, one address** | Shared resolution result, with service identity still unresolved |
| **Alias to a provider name** | A DNS dependency worth validating with the asset owner |
| **Child-zone delegation** | Separate authoritative data below the delegation point |
| **No public answer** | No answer from this query context, not proof no internal service exists |

## Understand Certificate Transparency

**Certificate transparency (CT)** makes submitted certificates and precertificates auditable through public logs. It supports monitoring issuance in the public web PKI ecosystem. It is not a complete database of every certificate, private PKI, or service endpoint. [Read how CT works](https://certificate.transparency.dev/howctworks/).

**Certificate names** provide historical naming evidence. A certificate containing **`portal.example.com`** suggests the name mattered to its requester at issuance, but does not prove a service is currently reachable there. A wildcard such as **`*.example.com`** does not enumerate all individual names covered by its pattern.

**Log duplicates** also need interpretation. One certificate submitted to several logs is not several independently observed servers. Preserve the certificate identity and source relationships when counting evidence.

| Certificate evidence | Supported statement | Unsupported leap |
|---|---|---|
| **Named entry** | A name appears in the recorded certificate | A live vulnerable server exists |
| **Wildcard entry** | A wildcard name was included | Every possible subdomain is deployed |
| **Expired certificate** | Historical issuance evidence exists | The associated service remains active |

## Treat Scan Data as Historical

**Shodan records** describe observations made by Shodan's collection systems. Their value comes from the captured service information and associated timestamps. A stored banner is not a new measurement from your current vantage point.

**Timeframes matter.** Shodan documents different historical windows across its services, with its principal search interfaces presenting recent banner observations within a defined rolling window. Read the record's collection timestamp and the interface's documented behavior before describing a result as current. [Read Shodan's data-timeframe documentation](https://help.shodan.io/mastery/data_timeline).

**Service identity needs corroboration.** An address might be reassigned, a reverse proxy might answer on behalf of several applications, or a banner might conceal the underlying version. A result is a lead for the approved validation plan, not automatic proof of ownership or vulnerability.

| Compare these times | Why they differ |
|---|---|
| **Observed at** | When the provider collected the source observation |
| **Retrieved at** | When you obtained the record |
| **Published at** | When a page or report became available |
| **Valid for decision** | Your stated freshness requirement for the research question |

## Choose Automation by Behavior

**SpiderFoot** provides modules for gathering and correlating information from multiple sources. Module selection, API access, and collection behavior affect what a run does. Review the selected modules before assuming a tool labeled “OSINT” only reads existing third-party records. [Read the project documentation](https://github.com/smicallef/spiderfoot).

**Tool choice** follows the question. A graph helps review relationships, a document parser extracts metadata, and a search service locates indexed material. None of those operations independently verifies the meaning of the resulting relationship.

**Rate and data limits** belong in the collection plan. Record provider limits, allowed input types, and the necessary output fields before automation. Avoid expanding from an approved domain investigation into unrelated personal profiles because a module offers more pivots.

| Need | Appropriate tool behavior | Review requirement |
|---|---|---|
| **Find published material** | Search an index | Verify the original source |
| **Correlate names** | Normalize and graph records | Preserve provenance and duplicates |
| **Extract document metadata** | Parse a saved public file | Distinguish metadata from verified identity |
| **Map exposure leads** | Read existing service observations | Check age, ownership, and scope |

## Normalize Without Inventing Evidence

**Normalization** removes superficial differences while preserving the original observations. Lowercasing a DNS name and removing its final root dot helps compare names. Treat a certificate wildcard separately instead of converting it into an invented host.

**Run this local example** with Python 3. It performs no network requests and writes no files. The output separates exact names from a wildcard certificate pattern.

```python
observations = [
    "Portal.Example.com.",
    "portal.example.com",
    "*.example.com",
    "status.example.com",
]

names = set()
wildcards = set()
for original in observations:
    normalized = original.lower().rstrip(".")
    if normalized.startswith("*."):
        wildcards.add(normalized)
    else:
        names.add(normalized)

print("Exact names:", ", ".join(sorted(names)))
print("Wildcard patterns:", ", ".join(sorted(wildcards)))
```

**Expected output** contains two distinct exact names and one wildcard pattern. The duplicate portal spelling collapses into one name, but your evidence ledger should retain both original source rows. Deduplication for counting is different from deleting provenance.

```text
Exact names: portal.example.com, status.example.com
Wildcard patterns: *.example.com
```

## Work an Evidence Case

**Illustrative case:** an assessment permits research about the fictional Example organization. The active-scan list contains **`status.example.com`** only. You collect the following synthetic records while investigating whether a second portal needs ownership review.

| Record | Observation | Collection context |
|---|---|---|
| **A** | Certificate names portal.example.com | Issued 18 months before review |
| **B** | Blog repeats the certificate name | Links directly to record A |
| **C** | Archived banner identifies a portal | Provider observed it 24 days earlier |
| **D** | Owner inventory lists a retired portal | Inventory updated this week |

**Analyze the evidence:** decide whether A and B independently corroborate the portal's current state. Identify the newest relevant record and the unresolved relationship between C and D. Then decide whether these records authorize scanning the portal.

**Expected reasoning:** B repeats A, so they share one underlying source. D is the newest inventory statement, while C reflects an earlier external observation. The apparent conflict might represent a retirement after collection, a stale inventory, or a mistaken service association.

**The next action** is ownership clarification through the assessment's agreed contact. The evidence supports asking about an unresolved exposure lead, not adding the portal to the scan list. A useful brief names the exact conflict and requests the smallest confirmation needed.

```text
Claim ID: OSINT-PORTAL-01
Question: Does the historical portal need approved exposure validation?
Supported facts: Certificate name, dated banner, retirement inventory entry
Shared sources: B derives from A
Uncertainty: Current state and relationship between C and D
Scope status: Not on the approved active-scan list
Next action: Ask the asset owner to reconcile the records
Evidence locations: A, B, C, D with source URLs and timestamps
```

## Assess Source Quality

**Independent corroboration** depends on origin, not website count. Ten articles repeating one press release still share a source. Follow citations backward and retain both the originating item and the later interpretation when the distinction matters.

**Visual evidence** also needs context. An image or video supports claims about what it depicts only after its origin, location, time, and relevant features are examined. Bellingcat's verification examples demonstrate checking an item's claimed context against other evidence. [Read its social-media verification guide](https://www.bellingcat.com/resources/2021/11/01/a-beginners-guide-to-social-media-verification/).

**Confidence** should explain reasoning rather than imply a calculated probability without a model. Use terms such as “supported historical observation,” “current owner confirmation,” and “unverified lead.” State what new evidence would change the conclusion.

| Quality question | Useful check |
|---|---|
| **Origin** | Locate the earliest identifiable source |
| **Freshness** | Compare collection time with the decision window |
| **Independence** | Trace whether sources copy one another |
| **Contradiction** | Record evidence challenging the preferred explanation |
| **Relevance** | Connect the observation to the research question |

## Watch the Toolkit Introduction

**Bellingcat's toolkit presentation** introduces resources for open-source investigation. Use it to choose a method for a defined question rather than collecting a long list of unrelated tools. For one demonstrated resource, write down its input, output, and verification limits.

{{< youtube id="-Y3GQ6mSGqM" enable="true" title="Presenting: The Bellingcat Online Open Source Investigations Toolkit" >}}

**Watch on YouTube:** [Presenting: The Bellingcat Online Open Source Investigations Toolkit](https://www.youtube.com/watch?v=-Y3GQ6mSGqM).

## Create Your Research Brief

**Build a one-page brief** from five synthetic observations. Include one duplicate source, one stale record, one conflicting record, and one item irrelevant to the research question. Explain which items affect the decision and which do not.

**Preserve a minimal evidence package** with source URLs, retrieval times, original records where appropriate, and the relevant excerpts. Avoid unnecessary personal information or secrets. If a public source appears to expose a credential, follow the agreed reporting process rather than treating availability as permission to use it.

| Brief section | Required content |
|---|---|
| **Question and scope** | What the research should answer and permitted next actions |
| **Evidence** | Observations with provenance and timestamps |
| **Analysis** | Corroboration, contradictions, and source dependencies |
| **Conclusion** | Supported answer and explicit uncertainty |
| **Next action** | Owner, requested clarification, or approved validation |

**Evaluate your brief** by asking another reader to reconstruct the reasoning from the preserved evidence. They should distinguish what you observed, what you inferred, and what remains unresolved. A persuasive paragraph without traceable sources is not a finished intelligence product.

## Check Your Understanding

1. **Collection:** does public availability guarantee an unobserved lookup?
2. **Registration:** why is an IP allocation record insufficient to establish scan scope?
3. **Certificates:** does a wildcard enumerate deployed hostnames?
4. **Corroboration:** do two websites repeating one certificate entry count as independent evidence?
5. **Freshness:** which timestamp describes when a scan provider observed a banner?

| Question | Expected reasoning |
|---|---|
| **Collection** | Providers and contacted systems have their own observation paths |
| **Registration** | Resource registration and assessment authorization are separate facts |
| **Certificates** | A wildcard is a naming pattern, not a host list |
| **Corroboration** | Shared origin limits independence |
| **Freshness** | The observation timestamp, distinct from your retrieval time |

## Next Steps

**Active reconnaissance** tests approved questions against current services. Continue to [Module 9: Active Reconnaissance and Scanning](/red-team-course/active-reconnaissance-and-scanning/) with a bounded target list and unresolved questions. Return to the [Red Team Course hub](/red-team-course-start/) for the full sequence.
