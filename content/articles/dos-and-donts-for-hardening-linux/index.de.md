---
title: "Essential Do's and Don'ts for Hardening Your Linux System"
date: 2023-02-28
toc: true
draft: false
description: "Learn the essential dos and donts for hardening your Linux system, including updating, using firewalls, enabling SELinux or AppArmor, configuring password policies, and monitoring system logs."
tags: ["Linux security", "system hardening", "firewall", "SELinux", "AppArmor", "password policy", "system updates", "system logs", "security modules", "access control policies", "cybersecurity", "system security", "network security", "vulnerability management", "security best practices", "IT security", "information security", "software updates", "root access", "password manager"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "A cartoon lock holding a shield with the word Linux on it, while an arrow bounces off the shield."
coverCaption: ""
---
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade

```
```bash
sudo yum update
```
```bash
sudo yum autoremove
```
```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```
```bash
sudo ufw allow http
```
```bash
sudo ufw deny from <ip_address>
```
```bash
sudo ufw delete <rule_number>
```
```bash
sudo ufw status
```
```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```
```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --list-all
```
```bash
sestatus
```
```bash
sudo yum install selinux-policy selinux-policy-targeted
```
```bash
sudo nano /etc/selinux/config
```
```
SELINUX=enforcing
```
```bash
sudo apparmor_status
```
```bash
sudo apt-get install apparmor
```
```bash
sudo nano /etc/default/grub
```
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```
```bash
sudo update-grub
```
```bash
sudo apt-get install libpam-pwquality
```
```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```
```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```
```bash
sudo journalctl
```
```bash
sudo journalctl -u sshd
```
```bash
sudo journalctl --since "1 hour ago"
```

  Linux ist ein beliebtes Betriebssystem, das von erwarteten und Unternehmen ähnlich verwendet WIRD. Obwohl es aufgrund seiner Open-Source-Natur oft als sicherer als andere Betriebssysteme angesehen wird, erfordert es dennoch eine Härtung, um die Sicherheit des Systems und der darin eingehenden Daten zu gewährleisten. In diesem Artikel gehen wir auf einige allgemeine Gebote und Verbote für die Härtung ein, die dazu beitragen können, Ihr Linux-System sicher zu halten.  ## Aufgaben:  ### Halten Sie Ihr System auf dem neuesten Stand  Es ist entscheidend, Ihr [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/)-System auf dem neuesten Stand zu halten, um seine Sicherheit aufrechtzuerhalten. Regelmäßige Updates helfen dabei, Sicherheitslücken und Fehler zu beheben und sicherzustellen, dass Ihr System vor potenziellen Angriffen geschützt bleibt. Hier sind einige Beispiele, wie Sie Ihr Linux-System mit dem Paketmanager **apt-get** oder **yum** aktualisieren:  #### Ubuntu mit apt-get aktualisieren  Um Ihr Ubuntu-System mit **apt-get** zu aktualisieren, öffnen Sie ein Terminalfenster und geben Sie Folgendes ein:  Dadurch werden die neuesten Paketlisten aus den Ubuntu-Paket-Repositorys heruntergeladen. Sobald dieser Befehl abgeschlossen ist, können Sie alle verfügbaren Updates mit dem folgenden installieren:   Dadurch werden alle verfügbaren Updates für Ihr System heruntergeladen und installiert.  ### Aktualisieren von CentOS mit lecker  Um Ihr CentOS-System mit **yum** zu aktualisieren, öffnen Sie ein Terminalfenster und geben Sie Folgendes ein:   Dadurch werden alle verfügbaren Updates für Ihr System heruntergeladen und installiert. Sie können auch den folgenden Befehl verwenden, um alle alten oder nicht verwendeten Pakete zu bereinigen:   Dadurch werden alle Pakete entfernt, die auf Ihrem System nicht mehr benötigt werden.  Denken Sie daran, regelmäßig nach Updates für Ihr Linux-System zu suchen und diese zu installieren, um dessen Sicherheit und Stabilität zu gewährleisten.   ### Verwenden Sie eine Firewall  Eine Firewall ist eine maßgebliche Sicherheitsmaßnahme für jedes Linux-System, da sie zum Schutz vor unbefugtem Zugriff und anderen Cyber-Bedrohungen erfolgt. Also verwenden SIE die **ufw**-Firewall auf Ihrem Linux-System:  #### ufw für Ubuntu-basierte Systeme installieren und aktivieren  Um **ufw** zu installieren und zu aktivieren, öffnen Sie ein Terminalfenster und geben Sie Folgendes ein:   So lassen Sie eingehenden HTTP-Datenverkehr (Port 80) zu:   So blockieren Sie eingehenden Datenverkehr von einer bestimmten IP-Adresse:   So löschen Sie eine Regel:  SIE kann die aktuellen **ufw**-Regeln anzeigen, gibt SIE dafür Folgendes ein:    Dadurch werden die aktuellen Regeln und deren Status angezeigt.  SIE DARAN, Ihre **ufw**-Regeln regelmäßig zu denken und zu aktualisieren, um sicherzustellen, dass Ihr System vor potenziellen Bedrohungen geschützt ist.   #### Firewalld für CentOS-basierte Systeme installieren und aktivieren  Um die Standard-Firewall auf CentOS, die **firewalld** ist, zu installieren und zu aktivieren, können SIE folgende Befehle verwenden:   Dadurch wird **firewalld** installiert und auf Ihrem System aktiviert.  #### Konfigurieren von Firewall-Regeln für CentOS-basierte Systeme  Sobald **firewalld** aktiviert ist, can SIE ihre Regeln konfigurieren, um eingehenden und ausgehenden Datenverkehr zuzulassen oder zu blockieren. Hier sind einige Beispiele:  So lassen Sie eingehenden SSH-Datenverkehr (Port 22) zu:   So lassen Sie eingehenden HTTP-Datenverkehr (Port 80) zu:   So blockieren Sie eingehenden Datenverkehr von einer bestimmten IP-Adresse:   So löschen Sie eine Regel:   Sie können die aktuellen **firewalld**-Regeln anzeigen, dafür geben SIE Folgendes ein:   Dadurch werden die aktuellen Regeln und deren Status angezeigt.  SIE DARAN, Ihre **firewalld**-Regeln zu Denken regelmäßig zu überprüfen und zu aktualisieren, um sicherzustellen, dass Ihr System  ### Aktivieren Sie SELinux oder AppArmor  SELinux (Security-Enhanced Linux) und AppArmor sind zwei Sicherheitsmodule, die verwendet werden können, um obligatorische Zugriffskontrollrichtlinien in Linux-Systemen durchzusetzen. Standardmäßig sind auf den meisten modernen Linux-Distributionen SELinux oder AppArmor installiert, die aktiviert und konfiguriert werden können, um die Sicherheit Ihres Systems zu erhöhen.  #### Aktivierung von SELinux für CentOS-basierte Systeme  Führen SIE den following Befehl aus, um zu überprüfen, ob SELinux auf Ihrem System aktiviert ist:   Wenn der Befehl der SELinux nicht installiert ist, können Sie es mit dem following installieren:   Um SELinux zu aktivieren, müssen Sie die Datei **/etc/selinux/config** bearbeiten und die Variable **SELinux** auf **enforcing** setzen:  **Änderung SELINUX=erzwingen**  Speichern und verlassen Sie die Datei mit STRG+X und Y, geben Sie sie ein und starten Sie Ihr System neu.  #### Aktivieren von AppArmor für Ubuntu-basierte Systeme  Führen SIE den folgenden Befehl aus, um zu überprüfen, ob AppArmor auf Ihrem System aktiviert ist:   Wenn der Befehl der AppArmor nicht installiert ist, können Sie es mit dem folgenden installieren:  Um AppArmor zu aktivieren, müssen SIE die Datei **/etc/default/grub** bearbeiten und den Parameter **security=apparmor** zur Variablen **GRUB_CMDLINE_LINUX** hinzufügen:  **Sicherheit hinzufügen=apparmor**  Speichern und beenden Sie die Datei mit STRG+X und Y, geben Sie sie ein und führen Sie dann den folgenden Befehl aus, um die Bootloader-Konfiguration Ihres Systems zu aktualisieren:   Starten Sie abschließend Ihr System neu.  Sobald SELinux oder AppArmor aktiviert sind, können SIE ihre Richtlinien konfigurieren, um die Berechtigungen von Prozessen einzuschränken und ihren Zugriff auf Systemressourcen zu beschränken. Dies kann dazu beitragen, die potenziellen Auswirkungen eines erfolgreichen Angriffs zu minimieren und die Gesamtsicherheit Ihres Systems zu verbessern.   ### Kennwortrichtlinien konfigurieren  Das Konfigurieren von Kennwortrichtlinien ist ein wichtiger Schritt zur Erhöhung der Sicherheit Ihres Linux-Systems. Indem Sie strenge Kennwortanforderungen durchsetzen, können Sie sicherstellen, dass Benutzerkonten sicher und vor potenziellen Angriffen geschützt sind. So konfigurieren Sie Kennwortrichtlinien auf Ihrem Linux-System:  #### Kennwortrichtlinien auf Ubuntu konfigurieren  Um Passwortrichtlinien auf Ubuntu zu konfigurieren, kann SIE das Modul **pam_pwquality** verwenden. Dieses Modul bietet eine Reihe von Überprüfungen der Passwortstärke, die zur Durchsetzung von Passwortrichtlinien used Werden can. Um das Modul **pam_pwquality** zu installieren, öffnen Sie ein Terminalfenster und geben Sie Folgendes ein:   Sobald das Modul installiert ist, können Sie seine Einstellungen konfigurieren, indem Sie die Datei **/etc/pam.d/common-password** bearbeiten. Um beispielsweise eine Mindestpasswortlänge von 8 Zeichen zu erzwingen und mindestens einen Großbuchstaben, Kleinbuchstaben, eine Ziffer und ein Sonderzeichen zu verlangen, kann SIE der Datei folgende Zeile hinzufügen:   Sie können auch andere Einstellungen konfigurieren, z. B. das maximale Kennwortalter, indem Sie der Datei Zeilen hinzufügen.  #### Passwortrichtlinien auf CentOS konfigurieren  Um Kennwortrichtlinien auf CentOS zu konfigurieren, können SIE das Tool **authconfig** verwenden. Dieses Tool bietet eine Reihe von Optionen, die zum Konfigurieren von Kennwortrichtlinien verwendet werden können. Um beispielsweise eine Mindestkennwortlänge von 8 Zeichen zu erzwingen und mindestens einen Großbuchstaben, Kleinbuchstaben, eine Ziffer und ein Sonderzeichen zu verlangen, kann SIE den folgenden Befehl verwenden:   Dadurch werden die Dateien **/etc/pam.d/system-auth** und **/etc/pam.d/password-auth** des Systems aktualisiert, um die angegebenen Kennwortrichtlinien durchzusetzen.  Denken Sie daran, Ihre Kennwortrichtlinien regelmäßig zu überprüfen und zu aktualisieren, um sicherzustellen, dass sie gegen potenzielle Angriffe wirksam bleiben.   ### Überwachen Sie Ihre Systemprotokolle  Die Überwachung Ihrer Systemprotokolle ist ein wichtiger Aspekt für die Überwachung der Sicherheit Ihres Linux-Systems. Systemprotokolle zeichnen Systemaktivitäten wie fehlgeschlagene Anmeldeversuche, Fehler und andere wichtige Ereignisse auf und können wertvolle Einblicke in potenzielle Sicherheitsbedrohungen oder andere Probleme geben, die Aufmerksamkeit erfordern. So überwachen Sie Ihre Systemprotokolle:  #### Mit dem Befehl journalctl  Auf den meisten modernen Linux-Distributionen können Sie den Befehl **journalctl** verwenden, um Systemprotokolle anzuzeigen. Dieser Befehl bietet eine Vielzahl von Optionen, die zum Filtern und Durchsuchen von Protokolleinträgen verwendet werden können.  Um alle Protokolleinträge anzuzeigen, führen Sie einfach den folgenden Befehl aus:   Dadurch werden alle Protokolleinträge angezeigt, wobei die neuesten Einträge ganz unten stehen.  Um Protokolleinträge nach einer bestimmten Einheit zu filtern, z. B. einem Dienst oder einem Prozess, can SIE sterben Option **-u ** weiter vom Namen der Einheit verwenden. Um beispielsweise Protokolleinträge für den Dienst **sshd** anzuzeigen, können SIE den Befehl ausführen:   Um Protokolleinträge nach einem bestimmten Zeitraum zu filtern, können Sie die Optionen **--seit** und **--until** von einem Zeitstempel oder Zeitraum verwenden. Um beispielsweise Protokolleinträge der letzten Stunde anzuzeigen, können Sie den folgenden ausführen:   #### Verwenden eines Protokollverwaltungstools  Bei größeren oder komplexeren Systemen kann es sinnvoll sein, ein Protokollverwaltungstool zum Sammeln und Analysieren von Systemprotokollen zu verwenden. Protokollverwaltungstools können erweiterte Funktionen wie Protokollüberwachung in Echtzeit, Protokollaggregation und Protokollanalyse bereitstellen und Ihnen dabei helfen, potenzielle Sicherheitsbedrohungen effizienter zu identifizieren und darauf zu reagieren.  Beispiele für Protokollverwaltungstools für Linux sind:  - **Logwatch**: ein einfaches Protokollanalysetool, das tägliche E-Mail-Zusammenfassungen von Systemprotokollen bereitstellt - **Logrotate**: ein Tool, das Protokolldateien automatisch rotiert und komprimiert, um Speicherplatz zu sparen - **ELK-Stack**: Ein beliebtes Open-Source-Protokollverwaltungstool, das Elasticsearch, Logstash und Kibana kombiniert, um Protokollüberwachungs- und -analysefunktionen in Echtzeit bereitzustellen  Denken Sie daran, Ihre Systemprotokolle regelmäßig zu überprüfen und zu analysieren, um potenzielle Sicherheitsbedrohungen rechtzeitig zu erkennen und darauf zu reagieren.  ______  ## Verbote:  ### Verwenden Sie schwache Passwörter  Die Verwendung schwacher Passwörter ist ein gescannter Fehler, der Ihr Linux-System anfällig für Angriffe machen kann. Angreifer can Tools verwenden, um Passwörter zu erraten, die auf gebräuchlichen Wörtern, Namen oder Daten basieren. Es ist wichtig, starke und eindeutige Passwörter zu verwenden, die nicht leicht zu erraten sind.  Sie können starke Passwörter erstellen, indem Sie eine Kombination aus Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen verwenden. Es ist auch eine gute Praxis, einen [Passwort-Manager] (https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) zu verwenden, um komplexe Passwörter sicher zu generieren und zu speichern. [Passwortmanager] (https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) können Ihnen auch dabei helfen, sich Ihre Passwörter zu merken und zu vermeiden, dass Sie dasselbe Passwort für mehrere Konten verwenden .  ### Root-SSH-Zugriff zulassen  Das Zulassen des Root-SSH-Zugriffs ist ein Sicherheitsrisiko, das Angreifern die vollständige Kontrolle über Ihr Linux-System geben kann. Stattdessen sollten SIE ein Nicht-Root-Benutzerkonto verwenden, um sich bei Ihrem System anzumelden, und dann die Berechtigungen mit dem Befehl **sudo** erhöhen. Dies trägt dazu bei, die potenziellen Auswirkungen eines Angriffs zu begrenzen, indem die Zugriffsrechte von Benutzerkonten eingeschränkt werden.  ### Unnötige Software installieren  Die Installation unnötiger Software kann die Angriffsfläche Ihres Linux-Systems vergrößern und es anfälliger für Angriffe machen. Es ist wichtig, nur Software zu installieren, sterben für Ihr System erforderlich ist, und unnötige Software zu entfernen. Dies trägt dazu bei, die Anzahl potenzieller Schwachstellen auf Ihrem System zu reduzieren und das Risiko eines erfolgreichen Angriffs zu minimieren.  ### Verwenden Sie veraltete Software  Die Verwendung veralteter Software kann Ihr System anfällig für Angriffe machen, die bekannten Schwachstellen ausnutzen. Es ist wichtig, immer die neueste Version der Software zu verwenden und diese regelmäßig zu aktualisieren, um die Sicherheit zu gewährleisten. Dies hilft, bekannte Schwachstellen zu patchen und Ihr System vor potenziellen Angriffen zu schützen.  ______  ## Abschluss  Zusammenfassend lässt sich sagen, dass die Härtung Ihres Linux-Systems maßgeblich IST, um seine Sicherheit zu gewährleisten und die darin enthaltenen Daten zu schützen. Indem Sie die in diesem Artikel beschriebenen Gebote und Verbote befolgen, können Sie wichtige Schritte unternehmen, um Ihr System zu sichern und das Risiko von Cyberbedrohungen zu verringern. Denken Sie daran, Ihr System immer auf dem neuesten Stand zu halten, eine Firewall zu verwenden, Kennwortrichtlinien zu konfigurieren und Systemprotokolle zu überwachen. Vermeiden Sie es, schwache Passwörter zu verwenden, automatische Updates zu deaktivieren, Root-SSH-Zugriff zuzulassen, unnötige Software zu installieren und veraltete Software zu verwenden. Mit diesen Best Practices können Sie sicherstellen, dass Ihr Linux-System sicher und geschützt bleibt.  ## Verweise:  - [Linux Hardening Guide des Center for Internet Security](https://www.cisecurity.org/cis-hardened-images/) - [Sicherheitshandbuch für Red Hat Enterprise Linux] (https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index) - [Ubuntu-Sicherheitsdokumentation] (https://ubuntu.com/security) - [Linux-Sicherheits-Wiki](https://en.wikibooks.org/wiki/Linux_Security)