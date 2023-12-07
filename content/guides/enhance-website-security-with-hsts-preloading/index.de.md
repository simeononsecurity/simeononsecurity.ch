---
title: "HSTS Preloading Wie man die Sicherheit einer Website verbessert: Eine Schritt-für-Schritt-Anleitung"
date: 2023-08-20
toc: true
draft: false
description: "Erfahren Sie, wie Sie die Sicherheit Ihrer Website und das Vertrauen der Nutzer verbessern können, indem Sie die HSTS-Einstellungen in Chrome und Firefox vorladen. Folgen Sie unserer Schritt-für-Schritt-Anleitung für eine nahtlose Implementierung."
cover: "/img/cover/enhanced-website-security.png"
coverAlt: "Eine Illustration einer Website im Cartoon-Stil, die mit einem Schloss versehen ist und für mehr Sicherheit und Schutz vor Cyber-Bedrohungen steht."
coverCaption: "Stärken Sie den Schutz Ihrer Website, indem Sie das HSTS-Preloading einführen."
---

## **Erhöhen Sie die Sicherheit Ihrer Website mit HSTS Preloading: Eine Schritt-für-Schritt-Anleitung**

HTTP Strict Transport Security (HSTS) ist ein **wichtiger Sicherheitsmechanismus**, der sicherstellt, dass Websites HTTPS-Verbindungen erzwingen, um **die Nutzer vor potenziellen Sicherheitsbedrohungen** zu schützen. Durch das Vorladen von HSTS-Einstellungen in Chrome und Firefox können Sie die **Websicherheit** erhöhen und das **Vertrauen der Nutzer** stärken. In diesem umfassenden Leitfaden führen wir Sie durch die **wesentlichen Schritte**, um Ihre HSTS-Einstellungen erfolgreich vorzuladen, und geben **nützliche Empfehlungen** zur Optimierung der Sicherheit.

______

**Verständnis des HSTS-Preloading**

**Beim **HSTS-Preloading** wird die Domain Ihrer Website **in die Preload-Listen der wichtigsten Browser aufgenommen. Einmal hinzugefügt, erzwingen diese Browser **automatisch HTTPS-Verbindungen** für Ihre Domain und alle Subdomains. Dadurch wird sichergestellt, dass die Benutzer immer sicher auf Ihre Website zugreifen können, und das Risiko von **Man-in-the-Middle-Angriffen** und unbefugtem Abhören wird verringert. Weitere Einzelheiten zum HSTS-Preloading finden Sie in der offiziellen [documentation](https://hstspreload.org/)

______

______

### **Voraussetzungen für die Einreichung**

Bevor Sie Ihre Domain für das HSTS-Preloading einreichen, stellen Sie sicher, dass Ihre Website die folgenden **wesentlichen Anforderungen** erfüllt:

1. **Gültiges Zertifikat**: Ihre Website muss über ein **gültiges SSL- oder TLS-Zertifikat** verfügen, um **sichere HTTPS-Verbindungen** zu ermöglichen.

2. **HTTP-zu-HTTPS-Umleitung**: Stellen Sie sicher, dass alle **HTTP-Anfragen** auf ihre **HTTPS-Gegenstücke** umgeleitet werden, wenn Ihre Website auf Port 80 lauscht.

3. **HTTPS für alle Subdomains**: Alle Subdomains Ihrer Website müssen **HTTPS-Verbindungen** unterstützen, um für das HSTS-Preloading in Frage zu kommen.

4. **HSTS-Header auf der Basisdomain**: Fügen Sie einen **HSTS-Header** auf Ihrer Basisdomain für HTTPS-Anfragen mit den folgenden Einstellungen ein:
   - `max-age` muss **mindestens 31536000 Sekunden** (1 Jahr) betragen.
   - Die `includeSubDomains` muss angegeben werden, um alle Subdomains einzuschließen.
   - Die `preload` muss angegeben werden, um die Aufnahme in die Preload-Liste zu beantragen.

Hier ist ein Beispiel für einen gültigen HSTS-Header:

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

______

### So laden Sie die HSTS-Einstellungen vor**

Wenn Ihre Website **vollständig auf HTTPS** umgestellt ist und die oben genannten Anforderungen erfüllt, befolgen Sie diese **wichtigen Schritte**, um Ihre HSTS-Einstellungen erfolgreich vorzuladen:

1. **Überprüfen Sie die Subdomains**: Stellen Sie sicher, dass alle **Subdomains Ihrer Website** korrekt über HTTPS funktionieren, um den Nutzern ein nahtloses Surferlebnis zu bieten.

2. **Schrittweises Hochfahren**: Um mögliche Probleme zu testen und zu beheben, fügen Sie den **HSTS-Header** zu Ihren HTTPS-Antworten mit einer **niedrigen `max-age` Wert** (z. B. 300 Sekunden). Erhöhen Sie schrittweise den `max-age` Wert in Stufen:
   - 5 Minuten: `max-age=300; includeSubDomains`
   - 1 Woche: `max-age=604800; includeSubDomains`
   - 1 Monat: `max-age=2592000; includeSubDomains`

3. **Metriken überwachen**: Überwachen Sie in jeder Phase **genau die Kennzahlen Ihrer Website**, einschließlich Besucherzahlen und Einnahmen, um eventuelle Probleme zu erkennen und zu beheben, bevor Sie mit der nächsten Phase fortfahren.

4. **Erhöhen Sie die maximale Laufzeit auf 2 Jahre**: Wenn Sie **sicher sind, dass es keine Probleme mehr gibt**, setzen Sie die `max-age` auf **2 Jahre (63072000 Sekunden)** und fügen Sie die `preload` Richtlinie in den HSTS-Header einfügen:
```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

5. **Einreichen Ihrer Website**: Nach der Implementierung der 2-Jahres `max-age` Einstellung, **tragen Sie Ihre Website** in die HSTS-Preload-Liste ein, indem Sie das Formular verwenden, das auf [hstspreload.org](https://hstspreload.org/) Beachten Sie, dass es mehrere Monate dauern kann, bis die Aufnahme in die Preload-Liste die Nutzer mit einem Chrome-Update erreicht.
______

### **Opt-In für HSTS-Preloading: Befähigung von Website-Betreibern**

Die Unterstützung des HSTS-Preloads ist eine **exzellente Sicherheitspraxis**, die den Schutz von Websites erhöht. Es sollte jedoch eine **Opt-In-Entscheidung** für Website-Betreiber sein. Wenn Sie **HTTPS-Konfigurationshinweise** geben oder eine Option zur Aktivierung von HSTS anbieten, **vermeiden Sie es, die `preload` Richtlinie standardmäßig**. Dieser Ansatz verhindert eine unbeabsichtigte Aufnahme in die Preload-Liste, was zu Schwierigkeiten beim Zugriff auf bestimmte Subdomains führen kann.

Um einen reibungslosen Ablauf zu gewährleisten, **informieren Sie Seitenbetreiber** über die **langfristigen Folgen** des Preloads und betonen Sie die **Wichtigkeit der Erfüllung aller Anforderungen**, bevor Sie HSTS für ihre Domain aktivieren.

______

### **Entfernung von der Preload-Liste: Eine bewusste Entscheidung**

Die Aufnahme in die Preload-Liste ist eine **permanente Entscheidung**, die nicht einfach rückgängig gemacht werden kann. Wenn jedoch **starke technische oder kostenbezogene Gründe** die HTTPS-Unterstützung für bestimmte Subdomains verhindern, haben Sie die Möglichkeit, die **Entfernung aus der Preload-Liste von Chrome** über die [removal form](https://hstspreload.org/removal/)

Vergewissern Sie sich, dass Sie die Auswirkungen sorgfältig geprüft haben, bevor Sie diese wichtige Entscheidung treffen.
______

______

**Sicheres Surfen beginnt mit HSTS-Preloading**

Zusammenfassend lässt sich sagen, dass das Vorladen der HSTS-Einstellungen in Chrome und Firefox ein **proaktiver Schritt** hin zu einem sichereren Web-Browsing-Erlebnis für Ihre Nutzer ist. Durch die **Verstärkung von HTTPS-Verbindungen** schützen Sie **sensible Daten** und bauen **Vertrauen** bei Ihren Besuchern auf. Befolgen Sie die oben genannten **Richtlinien**, um Ihre HSTS-Einstellungen **erfolgreich vorzuladen** und die **erhöhte Sicherheit Ihrer Website** zu genießen.

______

### Referenzen

1. [Chromium - HTTP Strict Transport Security (HSTS)](https://www.chromium.org/hsts/)
2. [HSTS Preload Submission](https://hstspreload.org/)
3. [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
4. [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security/)
