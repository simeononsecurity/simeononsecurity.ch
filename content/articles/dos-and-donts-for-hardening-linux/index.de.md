---
title: "Wesentliche Do's und Don'ts für die Absicherung Ihres Linux-Systems"
date: 2023-02-28
toc: true
draft: false
description: "Lernen Sie die wichtigsten Maßnahmen zur Absicherung Ihres Linux-Systems kennen, einschließlich Updates, Verwendung von Firewalls, Aktivierung von SELinux oder AppArmor, Konfiguration von Passwortrichtlinien und Überwachung von Systemprotokollen."
tags: ["Linux-Sicherheit", "Systemhärtung", "Firewall", "SELinux", "AppArmor", "Passwort-Richtlinie", "System-Updates", "Systemprotokolle", "Sicherheitsmodule", "Zugangskontrollrichtlinien", "Cybersicherheit", "Systemsicherheit", "Netzwerksicherheit", "Schwachstellenmanagement", "bewährte Sicherheitsverfahren", "IT-Sicherheit", "Informationssicherheit", "Software-Aktualisierungen", "Root-Zugang", "Passwort-Manager"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Ein Cartoon-Schloss, das ein Schild mit dem Wort Linux in der Hand hält, während ein Pfeil vom Schild abprallt."
coverCaption: ""
---


Linux ist ein beliebtes Betriebssystem, das von Privatpersonen und Unternehmen gleichermaßen genutzt wird. Obwohl es aufgrund seines Open-Source-Charakters oft als sicherer als andere Betriebssysteme gilt, muss es dennoch ordnungsgemäß gehärtet werden, um die Sicherheit des Systems und der darin gespeicherten Daten zu gewährleisten. In diesem Artikel gehen wir auf einige allgemeine Tipps und Tricks ein, die dazu beitragen können, Ihr Linux-System sicher zu machen.

## Do's:

### Halten Sie Ihr System auf dem neuesten Stand

Halten Sie Ihr [Linux](https://simeononsecurity.com/articles/how-do-i-learn-linux/) System auf dem neuesten Stand zu halten, ist entscheidend für die Aufrechterhaltung seiner Sicherheit. Regelmäßige Aktualisierungen helfen dabei, Sicherheitslücken und Fehler zu beheben, und sorgen dafür, dass Ihr System gegen mögliche Angriffe geschützt bleibt. Im Folgenden finden Sie einige Beispiele, wie Sie Ihr Linux-System mit dem Paketmanager **apt-get** oder **yum** aktualisieren können:

#### Aktualisierung von Ubuntu mit apt-get

Um Ihr Ubuntu-System mit **apt-get** zu aktualisieren, öffnen Sie ein Terminalfenster und geben Sie ein:
```bash
sudo apt-get update
```

Dadurch werden die neuesten Paketlisten aus den Ubuntu-Paketquellen heruntergeladen. Sobald dieser Befehl abgeschlossen ist, können Sie alle verfügbaren Aktualisierungen mit dem folgenden Befehl installieren:

```bash
sudo apt-get upgrade

```

Dadurch werden alle verfügbaren Updates für Ihr System heruntergeladen und installiert.

### CentOS mit yum aktualisieren

Um Ihr CentOS-System mit **yum** zu aktualisieren, öffnen Sie ein Terminalfenster und geben Sie ein:

```bash
sudo yum update
```

Dadurch werden alle verfügbaren Aktualisierungen für Ihr System heruntergeladen und installiert. Sie können auch den folgenden Befehl verwenden, um alte oder nicht verwendete Pakete zu bereinigen:

```bash
sudo yum autoremove
```

Dadurch werden alle Pakete entfernt, die auf Ihrem System nicht mehr benötigt werden.

Denken Sie daran, regelmäßig nach Updates für Ihr Linux-System zu suchen und diese zu installieren, um seine Sicherheit und Stabilität zu gewährleisten.


### Verwenden Sie eine Firewall

Eine Firewall ist eine wesentliche Sicherheitsmaßnahme für jedes Linux-System, da sie vor unbefugtem Zugriff und anderen Cyber-Bedrohungen schützt. Hier erfahren Sie, wie Sie die **ufw**-Firewall auf Ihrem Linux-System verwenden:

#### Installieren und Aktivieren von ufw für Ubuntu-basierte Systeme

Um **ufw** zu installieren und zu aktivieren, öffnen Sie ein Terminalfenster und geben Sie ein:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Um eingehenden HTTP-Verkehr (Port 80) zuzulassen:

```bash
sudo ufw allow http
```

Um eingehenden Datenverkehr von einer bestimmten IP-Adresse zu blockieren:

```bash
sudo ufw deny from <ip_address>
```

So löschen Sie eine Regel:
```bash
sudo ufw delete <rule_number>
```

Sie können die aktuellen **ufw**-Regeln anzeigen, indem Sie eingeben:

```bash
sudo ufw status
```


Dadurch werden die aktuellen Regeln und ihr Status angezeigt.

Denken Sie daran, Ihre **ufw**-Regeln regelmäßig zu überprüfen und zu aktualisieren, um sicherzustellen, dass Ihr System vor potenziellen Bedrohungen geschützt ist.


#### Installieren und Aktivieren von firewalld für CentOS-basierte Systeme

Um die Standard-Firewall unter CentOS, **firewalld**, zu installieren und zu aktivieren, können Sie die folgenden Befehle verwenden:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Dies installiert **firewalld** und aktiviert es auf Ihrem System.

#### Konfigurieren von Firewalld-Regeln für CentOS-basierte Systeme

Sobald **firewalld** aktiviert ist, können Sie seine Regeln konfigurieren, um ein- und ausgehenden Datenverkehr zuzulassen oder zu blockieren. Hier sind einige Beispiele:

Um eingehenden SSH-Verkehr (Port 22) zuzulassen:

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Um eingehenden HTTP-Verkehr (Port 80) zuzulassen:

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Um eingehenden Datenverkehr von einer bestimmten IP-Adresse zu blockieren:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

So löschen Sie eine Regel:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

Sie können die aktuellen **firewalld**-Regeln anzeigen, indem Sie eingeben:

```bash
sudo firewall-cmd --list-all
```

Dadurch werden die aktuellen Regeln und ihr Status angezeigt.

Denken Sie daran, Ihre **firewalld**-Regeln regelmäßig zu überprüfen und zu aktualisieren, um sicherzustellen, dass Ihr System

### Aktivieren Sie SELinux oder AppArmor

SELinux (Security-Enhanced Linux) und AppArmor sind zwei Sicherheitsmodule, die verwendet werden können, um verbindliche Zugriffskontrollrichtlinien in Linux-Systemen durchzusetzen. Die meisten modernen Linux-Distributionen sind standardmäßig mit SELinux oder AppArmor ausgestattet. Sie können aktiviert und konfiguriert werden, um die Sicherheit Ihres Systems zu erhöhen.

#### Aktivierung von SELinux für CentOS-basierte Systeme

Um zu überprüfen, ob SELinux auf Ihrem System aktiviert ist, führen Sie den folgenden Befehl aus:

```bash
sestatus
```

Wenn SELinux nicht installiert ist, können Sie es mit dem folgenden Befehl installieren:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Um SELinux zu aktivieren, müssen Sie die Datei **/etc/selinux/config** bearbeiten und die Variable **SELINUX** auf **enforcing** setzen:

```bash
sudo nano /etc/selinux/config
```
**SELINUX=erzwingen** ändern
```
SELINUX=enforcing
```

Speichern und beenden Sie die Datei mit STRG+X und Y, dann Enter, und starten Sie Ihr System neu.

#### Aktivieren von AppArmor für Ubuntu-basierte Systeme

Um zu überprüfen, ob AppArmor auf Ihrem System aktiviert ist, führen Sie den folgenden Befehl aus:
```bash
sudo apparmor_status
```


Wenn AppArmor nicht installiert ist, können Sie es mit dem folgenden Befehl installieren:
```bash
sudo apt-get install apparmor
```

Um AppArmor zu aktivieren, müssen Sie die Datei **/etc/default/grub** bearbeiten und den Parameter **security=apparmor** zu der Variablen **GRUB_CMDLINE_LINUX** hinzufügen:

```bash
sudo nano /etc/default/grub
```
**Sicherheit=Panzerung hinzufügen**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Speichern und beenden Sie die Datei mit STRG+X und Y und dann mit Enter. Führen Sie dann den folgenden Befehl aus, um die Bootloader-Konfiguration Ihres Systems zu aktualisieren:

```bash
sudo update-grub
```

Starten Sie schließlich Ihr System neu.

Sobald SELinux oder AppArmor aktiviert ist, können Sie deren Richtlinien so konfigurieren, dass die Berechtigungen von Prozessen eingeschränkt und ihr Zugriff auf Systemressourcen begrenzt wird. Dies kann dazu beitragen, die potenziellen Auswirkungen eines erfolgreichen Angriffs zu minimieren und die allgemeine Sicherheit Ihres Systems zu erhöhen.


### Konfigurieren Sie Passwortrichtlinien

Die Konfiguration von Kennwortrichtlinien ist ein wichtiger Schritt, um die Sicherheit Ihres Linux-Systems zu erhöhen. Indem Sie strenge Kennwortanforderungen durchsetzen, können Sie sicherstellen, dass Benutzerkonten sicher und vor potenziellen Angriffen geschützt sind. Im Folgenden erfahren Sie, wie Sie Passwortrichtlinien auf Ihrem Linux-System konfigurieren:

#### Konfigurieren von Kennwortrichtlinien unter Ubuntu

Um Passwortrichtlinien unter Ubuntu zu konfigurieren, können Sie das Modul **pam_pwquality** verwenden. Dieses Modul bietet eine Reihe von Passwortstärkeprüfungen, die zur Durchsetzung von Passwortrichtlinien verwendet werden können. Um das Modul **pam_pwquality** zu installieren, öffnen Sie ein Terminalfenster und geben Sie ein:

```bash
sudo apt-get install libpam-pwquality
```

Sobald das Modul installiert ist, können Sie seine Einstellungen konfigurieren, indem Sie die Datei **/etc/pam.d/common-password** bearbeiten. Um beispielsweise eine Mindestlänge des Passworts von 8 Zeichen zu erzwingen und mindestens einen Großbuchstaben, einen Kleinbuchstaben, eine Ziffer und ein Sonderzeichen zu verlangen, können Sie die folgende Zeile in die Datei einfügen:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

Sie können auch andere Einstellungen, wie z. B. das maximale Alter des Kennworts, konfigurieren, indem Sie der Datei Zeilen hinzufügen.

#### Konfigurieren von Passwortrichtlinien unter CentOS

Um Passwortrichtlinien unter CentOS zu konfigurieren, können Sie das Tool **authconfig** verwenden. Dieses Tool bietet eine Reihe von Optionen, die zur Konfiguration von Passwortrichtlinien verwendet werden können. Um zum Beispiel eine Mindestlänge von 8 Zeichen für Passwörter zu erzwingen und mindestens einen Großbuchstaben, einen Kleinbuchstaben, eine Ziffer und ein Sonderzeichen zu verlangen, können Sie den folgenden Befehl verwenden:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Dadurch werden die Dateien **/etc/pam.d/system-auth** und **/etc/pam.d/password-auth** des Systems aktualisiert, um die angegebenen Passwortrichtlinien durchzusetzen.

Denken Sie daran, Ihre Kennwortrichtlinien regelmäßig zu überprüfen und zu aktualisieren, um sicherzustellen, dass sie gegen potenzielle Angriffe wirksam bleiben.


### Überwachen Sie Ihre Systemprotokolle

Die Überwachung Ihrer Systemprotokolle ist ein wichtiger Aspekt bei der Aufrechterhaltung der Sicherheit Ihres Linux-Systems. Systemprotokolle zeichnen Systemaktivitäten auf, wie z. B. fehlgeschlagene Anmeldeversuche, Fehler und andere wichtige Ereignisse, und können wertvolle Hinweise auf potenzielle Sicherheitsbedrohungen oder andere Probleme liefern, die Aufmerksamkeit erfordern. Im Folgenden erfahren Sie, wie Sie Ihre Systemprotokolle überwachen können:

#### Verwenden Sie den Befehl journalctl

Bei den meisten modernen Linux-Distributionen können Sie den Befehl **journalctl** verwenden, um Systemprotokolle einzusehen. Dieser Befehl bietet eine Reihe von Optionen, mit denen Sie Protokolleinträge filtern und durchsuchen können.

Um alle Protokolleinträge anzuzeigen, führen Sie einfach den folgenden Befehl aus:

```bash
sudo journalctl
```

Dadurch werden alle Protokolleinträge angezeigt, wobei die neuesten Einträge ganz unten stehen.

Um Protokolleinträge nach einer bestimmten Einheit zu filtern, z. B. einem Dienst oder einem Prozess, können Sie die Option **-u** gefolgt vom Namen der Einheit verwenden. Um beispielsweise Protokolleinträge für den Dienst **sshd** anzuzeigen, können Sie den folgenden Befehl ausführen:
```bash
sudo journalctl -u sshd
```


Um Protokolleinträge nach einem bestimmten Zeitbereich zu filtern, können Sie die Optionen **--since** und **--until**, gefolgt von einem Zeitstempel oder einem Zeitbereich, verwenden. Um beispielsweise die Protokolleinträge der letzten Stunde anzuzeigen, können Sie den folgenden Befehl ausführen:

```bash
sudo journalctl --since "1 hour ago"
```

#### Verwendung eines Protokollverwaltungstools

Bei größeren oder komplexeren Systemen kann es sinnvoll sein, ein Protokollverwaltungstool zum Sammeln und Analysieren von Systemprotokollen zu verwenden. Protokollverwaltungstools können erweiterte Funktionen bieten, z. B. Protokollüberwachung in Echtzeit, Protokollaggregation und Protokollanalyse, und können Ihnen helfen, potenzielle Sicherheitsbedrohungen effizienter zu erkennen und darauf zu reagieren.

Beispiele für Protokollverwaltungstools für Linux sind:

- **Logwatch**: ein einfaches Tool zur Protokollanalyse, das täglich per E-Mail Zusammenfassungen der Systemprotokolle liefert
- **Logrotate**: ein Tool, das Protokolldateien automatisch rotiert und komprimiert, um Speicherplatz zu sparen
- ELK-Stack**: ein beliebtes Open-Source-Tool für die Protokollverwaltung, das Elasticsearch, Logstash und Kibana kombiniert, um Protokollüberwachungs- und -analysefunktionen in Echtzeit bereitzustellen

Denken Sie daran, Ihre Systemprotokolle regelmäßig zu überprüfen und zu analysieren, um potenzielle Sicherheitsbedrohungen rechtzeitig zu erkennen und darauf zu reagieren.

______

## Don'ts:

### Schwache Passwörter verwenden

Die Verwendung schwacher Passwörter ist ein häufiger Fehler, der Ihr Linux-System anfällig für Angriffe machen kann. Angreifer können Tools verwenden, um Passwörter zu erraten, die auf allgemeinen Wörtern, Namen oder Daten basieren. Es ist wichtig, starke und eindeutige Passwörter zu verwenden, die nicht leicht zu erraten sind.

Sie können sichere Kennwörter erstellen, indem Sie eine Kombination aus Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen verwenden. Es ist auch eine gute Praxis, ein [password manager](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) kann Ihnen auch dabei helfen, sich Ihre Passwörter zu merken und zu vermeiden, dass Sie das gleiche Passwort für mehrere Konten verwenden.

### SSH-Zugang für root zulassen

Der SSH-Zugang von root ist ein Sicherheitsrisiko, das Angreifern die vollständige Kontrolle über Ihr Linux-System ermöglichen kann. Stattdessen sollten Sie ein Nicht-Root-Benutzerkonto verwenden, um sich bei Ihrem System anzumelden und dann die Rechte mit dem Befehl **sudo** zu erhöhen. Dies trägt dazu bei, die potenziellen Auswirkungen eines Angriffs zu begrenzen, indem die Berechtigungen der Benutzerkonten eingeschränkt werden.

### Unnötige Software installieren

Die Installation unnötiger Software kann die Angriffsfläche Ihres Linux-Systems vergrößern und es damit anfälliger für Angriffe machen. Es ist wichtig, nur Software zu installieren, die für Ihr System notwendig ist, und unnötige Software zu entfernen. Auf diese Weise können Sie die Anzahl potenzieller Schwachstellen in Ihrem System reduzieren und das Risiko eines erfolgreichen Angriffs minimieren.

### Verwenden Sie veraltete Software

Die Verwendung veralteter Software kann Ihr System anfällig für Angriffe machen, die bekannte Schwachstellen ausnutzen. Es ist wichtig, immer die neueste Softwareversion zu verwenden und sie regelmäßig zu aktualisieren, um die Sicherheit zu gewährleisten. Dadurch werden bekannte Sicherheitslücken geschlossen und Ihr System vor potenziellen Angriffen geschützt.

______

## Schlussfolgerung

Zusammenfassend lässt sich sagen, dass die Absicherung Ihres Linux-Systems von entscheidender Bedeutung ist, um seine Sicherheit zu gewährleisten und die darin gespeicherten Daten zu schützen. Wenn Sie sich an die in diesem Artikel beschriebenen Regeln halten, können Sie wichtige Schritte unternehmen, um Ihr System zu sichern und das Risiko von Cyber-Bedrohungen zu verringern. Denken Sie daran, Ihr System immer auf dem neuesten Stand zu halten, eine Firewall zu verwenden, Passwortrichtlinien zu konfigurieren und Systemprotokolle zu überwachen. Vermeiden Sie die Verwendung schwacher Passwörter, die Deaktivierung automatischer Updates, die Gewährung von SSH-Root-Zugriff, die Installation unnötiger Software und die Verwendung veralteter Software. Mit diesen bewährten Verfahren können Sie sicherstellen, dass Ihr Linux-System sicher und geschützt bleibt.

## Referenzen:

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)
