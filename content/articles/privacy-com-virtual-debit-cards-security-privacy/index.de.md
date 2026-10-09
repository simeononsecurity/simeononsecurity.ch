---
title: "Privacy.com Virtuelle Karten: Wie Zahlungsschutz funktioniert"
date: 2023-09-03
lastmod: 2026-10-08
toc: true
draft: false
description: Was auf einer Zahlungskarte gespeichert ist, warum der Magnetstreifen der schwächste Teil ist, was ein Händler sieht, wenn Sie mit einer virtuellen Nummer bezahlen, und wie die Kartentypen und Limits von Privacy.com in der Praxis funktionieren.
genre:
- Zahlungssicherheit
- Digitale Privatsphäre
- Virtuelle Karten
- Finanzielle Privatsphäre
- Betrugsprävention
- Verbrauchersicherheit
tags:
- privacy.com
- virtuelle Karten
- virtuelle Debitkarten
- Einmalkarten
- Händlergebundene Karten
- Kategoriegebundene Karten
- Tokenisierung
- Netzwerk-Token
- PAN
- CVV
- Kartendiebstahl
- Magnetstreifen
- Spur 1
- Spur 2
- Zahlungskartensicherheit
- Kreditkartenbetrug
- Abonnementverwaltung
- Ausgabenlimits
- PCI DSS
- SOC 2
- Karten-nicht-anwesend-Betrug
- finanzielle Privatsphäre
- Zahlungsprivatsphäre
- virtuelle Kartennummer
- maskierte Karte
- Karteneinstellungen
cover: /img/cover/privacy_virtual_cards.webp
coverAlt: Eine digitale Illustration zeigt eine geschützte virtuelle Karte, die ein Schloss-Symbol schützt und die Sicherheit und Privatsphäre virtueller Debitkarten darstellt.
coverCaption: Schützen, Kontrollieren und Sichern Sie Ihre Online-Transaktionen.
ref:
- /magnetic-stripe-decoder
- /articles/personal-security-checklist-prioritized-2026
- /personal-security-course/personal-finance
---

**Eine virtuelle Karte macht genau eines: Sie ändert, was der Händler erhält, nicht was Ihre Bank weiß.** Dies ist der gesamte Mechanismus, und das Verständnis erklärt sowohl den Schutz, den Sie erhalten, als auch den Schutz, den Sie nicht erhalten.

Die meisten Berichte behandeln virtuelle Karten als allgemeines Datenschutzwerkzeug und überspringen technische Details. Dieser Artikel erklärt, was auf einer Karte gespeichert ist, warum der Magnetstreifen der Schwachpunkt ist und wie die Kartentypen von Privacy.com in der Praxis funktionieren.

*Der praktische Nutzen ist eng und real: Eine gestohlene Nummer wird für einen Dieb nutzlos, weil sie nur beim Händler funktioniert, für den sie ausgestellt wurde.*

## Die kurze Antwort

| Frage | Kurze Antwort |
|---|---|
| **Was ändert eine virtuelle Karte?** | Die Nummer, die der Händler speichert. Ihre echten Kartendaten erreichen ihn nie |
| **Ist die Transaktion privat?** | Nein. Ihre Bank, das Netzwerk und der Aussteller sehen sie weiterhin |
| **Was verhindert, dass ein Datenleck Ihnen schadet?** | Eine händlergebundene oder Einmalkarte, die anderswo nicht funktioniert |
| **Was ist der schwächste Teil einer physischen Karte?** | Der Magnetstreifen, der die vollständigen Spurdaten unverschlüsselt speichert |
| **Baut sie Kredit auf?** | Nein. Es sind keine Kreditkonten und es erfolgt keine Bonitätsprüfung |
| **Wer kann Privacy.com nutzen?** | US-Bürger oder rechtmäßige Einwohner, 18+, mit einem US-Bank- oder Kreditgenossenschaftskonto |

## Was auf einer Zahlungskarte ist

**Drei Dinge autorisieren eine Karten-nicht-anwesend-Transaktion: die primäre Kontonummer, das Ablaufdatum und der Verifizierungswert.**

| Element | Länge | Herkunft |
|---|---|---|
| **Primäre Kontonummer (PAN)** | Bis zu 19 Ziffern | Vom Aussteller, mit führenden Ziffern zur Identifikation des Schemas und der Bank |
| **Ablaufdatum** | Vier Ziffern als MM/JJ | Vom Aussteller |
| **CVV oder CVC** | Drei oder vier Ziffern | Abgeleitet von PAN, Ablaufdatum und einem Schlüssel, den nur der Aussteller kennt |
| **Name des Karteninhabers** | Bis zu 26 Zeichen | Nur auf Spur 1 des Magnetstreifens sichtbar |

**Die PAN ist kein zufälliger String.** Die erste Ziffer identifiziert das Schema, die nächsten mehrere die ausstellende Bank, und der Rest identifiziert das Konto. Die Struktur ermöglicht eine Plausibilitätsprüfung der Kartennummer ohne Kontakt und erklärt, warum die Luhn-Prüfziffer eine einzelne vertauschte Ziffer erkennt.

**Der CVV beweist, dass jemand die Karte physisch besaß**, als sie ausgestellt wurde. Er wird nicht auf dem Magnetstreifen gespeichert, weshalb ein Skimmer, der den Streifen kopiert, ihn nie erhält.

*Untersuchen Sie das alles selbst mit dem **[Magnetstreifen-Decoder und -Encoder](/magnetic-stripe-decoder/)**, der Spur 1 und Spur 2 analysiert, die Servicecode-Ziffern dekodiert und das Ergebnis neu kodiert. Er läuft vollständig in Ihrem Browser, was wichtig ist, da dies der vollständige Inhalt einer Zahlungskarte ist.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Diagramm zeigt die Elemente einer Zahlungskarte einschließlich der primären Kontonummer, des Ablaufdatums, CVV und der drei Magnetstreifenspuren mit deren Inhalten" >}}

## Warum der Magnetstreifen der Schwachpunkt ist

**Der Streifen speichert Kontodaten im Klartext, und jeder kompatible Leser kann sie auslesen.**

Ein Magnetstreifen enthält bis zu drei Spuren. Spur 1 enthält PAN, Karteninhabername, Ablaufdatum und einen dreistelligen Servicecode und ist die einzige Spur mit alphabetischem Text. Spur 2 enthält PAN, Ablaufdatum und Servicecode in dichterer numerischer Kodierung, und **Spur 2 wird von fast jedem Kassenterminal gelesen.** Spur 3 wird von den großen Netzwerken praktisch nicht genutzt und ist oft gar nicht auf der Karte vorhanden.

Der Servicecode ist wichtig, weil er die erlaubte Nutzung der Karte beschreibt. Ziffer eins regelt Interchange-Regeln, Ziffer zwei die Autorisierungsbehandlung und Ziffer drei den Serviceumfang. Eine Karte mit Code `201` erlaubt internationalen Interchange, benötigt keinen speziellen Autorisierungspfad und hat keine Serviceeinschränkungen.

Die Geschichte erklärt, warum der Streifen so lange hielt. 1969 versuchte ein IBM-Ingenieur namens Forrest Parry, Magnetband auf eine Plastikkarte zu kleben, scheiterte aber daran, es ohne Beschädigung zu befestigen. Seine Frau schlug vor, ein Bügeleisen zu verwenden, und die Hitze verband das Band mit der Karte. Diese Improvisation wurde über ein halbes Jahrhundert Standard.

Zwei Entwicklungen beenden das:

| Meilenstein | Status |
|---|---|
| **Mastercard kündigte die Entfernung des Streifens an** | Bis 2033 werden keine Mastercard-Kredit- oder Debitkarten mehr einen Streifen haben |
| **Europa** | Streifen verschwinden seit 2024 von Mastercard-Karten |
| **USA** | Banken stellen ab 2027 die Ausgabe ein |

*Der Streifen wurde durch Chip- und kontaktloses Bezahlen ersetzt, weil das Kopieren keine besondere Fähigkeit außer einem Leser erfordert. Unser **[Magnetstreifen-Tool](/magnetic-stripe-decoder/)** zeigt, wie wenig Daten nötig sind, um eine funktionierende Spur zu rekonstruieren.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Diagramm eines Magnetstreifens zeigt die physische Position der Spuren eins, zwei und drei mit dem Feldlayout jeder Spur einschließlich Start- und Endzeichen, PAN, Name, Ablaufdatum und Servicecode" >}}

## Wie man Spurdaten liest

**Ein Magnetstreifen-String ist eine Folge von Feldern, nicht eine zweite Kartennummer.** Der Leser findet das Startzeichen, trennt die Felder, liest Ablaufdatum und Servicecode, prüft das Endzeichen und die LRC.

| Spur | Anfang | Hauptfelder | Ende | Zeichensatz |
|---|---|---|---|---|
| **Spur 1** | `%` | Formatcode, PAN, Name, Ablaufdatum, Servicecode, freier Datenbereich | `?` plus LRC | Sechs-Bit ALPHA, daher enthält es Buchstaben |
| **Spur 2** | `;` | PAN, Ablaufdatum, Servicecode, freier Datenbereich | `?` plus LRC | Vier-Bit BCD, daher enthält es Ziffern und eine kleine Menge an Satzzeichen |

Die optionalen Begrenzungszeichen kennzeichnen die physischen Datensatzgrenzen. Ein Decoder lässt sie oft weg, wenn er die Felder anzeigt, aber ein physischer Encoder benötigt das vollständige Datensatzformat, das vom Leser erwartet wird.

### Beispiel Spur 1

Dies ist ein synthetisches Beispiel. Es verwendet die standardmäßige Test-PAN aus dem Tool sowie einen gefälschten Namen, Ablaufdatum, Servicecode und freien Datenbereich. Es handelt sich nicht um eine Privacy.com-Karte und keine gültigen Zahlungsdaten.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Lesen Sie es von links nach rechts:

| Segment | Wert | Bedeutung |
|---|---|---|
| **Startbegrenzungszeichen** | `%` | Spur 1 Datensatz beginnt |
| **Formatcode** | `B` | Finanzkartenformat B |
| **PAN** | `4111111111111111` | Synthetische primäre Kontonummer |
| **Feldtrenner** | `^` | PAN endet und Name beginnt |
| **Name** | `TEST/USER` | Nachname, Trenner, Vorname |
| **Feldtrenner** | `^` | Name endet und Transaktionsfelder beginnen |
| **Ablaufdatum** | `2912` | Dezember 2029 im YYMM-Format |
| **Servicecode** | `501` | Nationaler Austausch, normale Verarbeitung, keine Einschränkungen |
| **Freier Datenbereich** | `0000000` | Vom Aussteller definierter Füllbereich in diesem Beispiel |
| **Endbegrenzungszeichen** | `?` | Spur 1 Daten enden vor dem LRC |

Der tatsächlich codierte Datensatz enthält auch ein LRC-Zeichen nach dem Endbegrenzungszeichen, wenn der Leser dies erwartet. Die sichtbare Textform ist nützlich zum Studium der Struktur. Die Bit-Ebene-Darstellung enthält außerdem ungerade Parität für jedes Zeichen.

### Beispiel Spur 2

Spur 2 entfernt den Namen und den Formatcode. Die gleichen synthetischen Werte lauten:

```text
;4111111111111111=291250100000000?
```

| Segment | Wert | Bedeutung |
|---|---|---|
| **Startbegrenzungszeichen** | `;` | Spur 2 Datensatz beginnt |
| **PAN** | `4111111111111111` | Synthetische primäre Kontonummer |
| **Trenner** | `=` | PAN endet und Transaktionsfelder beginnen |
| **Ablaufdatum** | `2912` | Dezember 2029 im YYMM-Format |
| **Servicecode** | `501` | Gleicher synthetischer Servicecode wie Spur 1 |
| **Freier Datenbereich** | `0000000` | Vom Aussteller definierter Füllbereich in diesem Beispiel |
| **Endbegrenzungszeichen** | `?` | Spur 2 Daten enden vor dem LRC |

**Spur 2 ist kürzer, weil sie keinen Karteninhabernamen enthält.** Viele Terminals lesen Spur 2 für gewöhnliche Durchzieh-Transaktionen, während Spur 1 das Namensfeld liefert, wenn ein Leser es anfordert.

### Service-Code Ziffern

**Die drei Service-Code Ziffern beschreiben das Terminal- und Autorisierungsverhalten.** Sie enthalten nicht den CVV, und eine Änderung an einer echten Karte ohne Genehmigung des Ausstellers führt zu ungültigen oder irreführenden Zahlungsdaten.

| Ziffer | Werte | Was sie beschreibt |
|---|---|---|
| **Erste** | `0`, `1`, `2`, `5`, `6`, `7`, `9` | Austauschregeln und Chip-Präferenz |
| **Zweite** | `0`, `1`, `2`, `4` | Autorisierungspfad |
| **Dritte** | `0` bis `7` | PIN, Bargeld, Waren- und Dienstleistungseinschränkungen |

**Die erste Ziffer** betrifft Austausch und Chip-Präferenz:

| Wert | Bedeutung |
|---|---|
| `0` | Nationale Verwendung |
| `1` | Internationaler Austausch erlaubt |
| `2` | Internationaler Austausch, Chip (IC) verwenden, wo möglich |
| `5` | Nur nationaler Austausch außer bei bilateralen Vereinbarungen |
| `6` | Nur nationaler Austausch außer bei bilateralen Vereinbarungen, Chip verwenden, wo möglich |
| `7` | Kein Austausch außer bei bilateralen Vereinbarungen (geschlossenes System) |
| `9` | Test |

**Die zweite Ziffer** betrifft die Autorisierungsabwicklung:

| Wert | Bedeutung |
|---|---|
| `0` | Normale Autorisierung |
| `1` | Normale Autorisierung |
| `2` | Online-Kontakt zum Aussteller |
| `4` | Online-Kontakt zum Aussteller außer bei bilateralen Vereinbarungen |

**Die dritte Ziffer** betrifft Dienstleistungseinschränkungen:

| Wert | Bedeutung |
|---|---|
| `0` | Keine Einschränkungen, PIN erforderlich |
| `1` | Keine Einschränkungen |
| `2` | Nur Waren und Dienstleistungen (kein Bargeld) |
| `3` | Nur Geldautomat, PIN erforderlich |
| `4` | Nur Bargeld |
| `5` | Nur Waren und Dienstleistungen (kein Bargeld), PIN erforderlich |
| `6` | Keine Einschränkungen, PIN verwenden, wo möglich |
| `7` | Nur Waren und Dienstleistungen (kein Bargeld), PIN verwenden, wo möglich |

Zum Beispiel bedeutet `201` internationalen Austausch mit Chip-Einsatz, wo möglich, normale Autorisierungsverarbeitung und keine Dienstleistungseinschränkungen. Der Decoder zeigt jede Ziffer einzeln an, sodass Sie die Tabelle nicht auswendig lernen müssen.

### LRC und Parität

**Der LRC ist ein Prüfzeichen, kein weiteres zu erfindendes Feld.** Der Encoder XOR-verknüpft den Datenwert jedes Zeichens vom Startbegrenzungszeichen bis zum Endbegrenzungszeichen. Er wandelt das Ergebnis zurück in den druckbaren Zeichensatz der Spur und meldet die codierten ungeraden Paritätsbits separat.

Spur 1 verwendet einen sechs-Bit ALPHA-Zeichensatz. Sein Datenwert ist der ASCII-Code minus `0x20`. Spur 2 verwendet einen vier-Bit BCD-Zeichensatz. Sein Datenwert ist das niederwertige Nibble des ASCII-Codes. Die Anwendung der Spur 1-Zuordnung auf Spur 2 ergibt einen falschen LRC.

Die Decoder-Option **Berechneten LRC einschließen** fügt das druckbare LRC-Zeichen zur Ausgabe hinzu. Die Aufschlüsselung zeigt auch das LRC-Bitmuster mit ungerader Parität. Verwenden Sie dies, um zu lernen, wie ein Leser den Datensatz prüft, nicht um die Kontrollen eines Ausstellers zu umgehen.

## Schreiben synthetischer Karten zum Testen

**Verwenden Sie den Decoder, um Teststrings zu schreiben, nicht echte Zahlungskarten.** Das Tool akzeptiert Felder, baut Spur 1 und Spur 2 neu auf, fügt optionale Begrenzungszeichen hinzu und berechnet den LRC. Es läuft lokal im Browser.

1. Öffnen Sie den **[Magnetic Stripe Decoder and Encoder](/magnetic-stripe-decoder/)**.
2. Wählen Sie **Load Test Card**. Dadurch wird das Tool mit der synthetischen PAN `4111111111111111`, dem Namen `TEST/USER`, dem Ablaufdatum `2912`, dem Servicecode `201` und Test-Diskretionärdaten gefüllt.
3. Aktivieren Sie **Include start and end sentinels**, um die physischen Datensatzgrenzen anzuzeigen.
4. Aktivieren Sie **Include calculated LRC**, um das berechnete Prüfzeichen anzuhängen.
5. Aktivieren Sie **Split discretionary data into PVKI, PVV and CVV** nur, um zu sehen, wie ein neunstelliger synthetischer Bereich dargestellt wird. Diese Bezeichnungen sind Herausgeberkonventionen, kein universelles Track-1- oder Track-2-Layout.
6. Ändern Sie den Namen, das Ablaufdatum, den Servicecode oder die synthetischen Diskretionärdaten. Die Ausgabe aktualisiert sich während der Eingabe.
7. Vergleichen Sie die decodierten Felder mit den generierten Zeichenfolgen. Löschen Sie die Felder nach Abschluss.

Für eine synthetische Track-1-Übung verwenden Sie:

```text
PAN: 4111111111111111
Surname: TEST
First name: USER
Expiry: 12/29
Service code: 201
Discretionary data: 000000000
```

Für eine synthetische Track-2-Übung verwenden Sie dieselbe PAN, dasselbe Ablaufdatum, denselben Servicecode und ein numerisches Diskretionärfeld. Die generierte Track-2-Zeichenfolge lässt den Namen weg, da Track 2 kein Namensfeld hat.

**Kopieren Sie keine echte Privacy.com-PAN, Ablaufdatum, CVV oder Diskretionärwerte auf eine beschreibbare Karte.** Privacy.com beschreibt sein Produkt als virtuelle Kartennummern, die über die Website oder App erstellt werden. Die offizielle Seite präsentiert den Dienst nicht als Magnetstreifenschreibsystem, und eine virtuelle Kartennummer ist kein Beweis für einen vom Herausgeber autorisierten physischen Streifen. Eine beschreibbare Testkarte mit echten Zugangsdaten erzeugt ein doppeltes Zahlungsmittel und verstößt gegen Herausgeberbedingungen oder Zahlungsregeln.

Die sichere Grenze ist einfach: Verwenden Sie die integrierte synthetische Probe des Tools, verwenden Sie eine Labor-Karte mit Dummy-Werten und verwenden Sie eine vom Herausgeber genehmigte physische Karte, wenn Sie persönlich bezahlen müssen. Versuchen Sie nicht, eine Privacy.com-Virtuelle Karte in eine physische Swipe-Karte umzuwandeln.

## Was eine virtuelle Karte verändert

**Eine virtuelle Karte ist eine zweite Nummer, die vor der ersten steht.**

Wenn Sie mit einer virtuellen Karte bezahlen, erhält der Händler eine Nummer, ein Ablaufdatum und einen CVV, die zur virtuellen Karte gehören. Ihre echte PAN erreicht ihn nie. Praktisch zeigt sich die Änderung nach einer Sicherheitsverletzung:

| Szenario | Mit Ihrer echten Karte | Mit einer auf den Händler gesperrten virtuellen Karte |
|---|---|---|
| **Händlerdatenbank geleakt** | Die Nummer ist überall gültig, wo sie akzeptiert wird | Die Nummer schlägt bei jedem anderen Händler fehl |
| **Abonnement, das Sie gekündigt haben** | Belastungen laufen weiter, bis Sie widersprechen | Sie schließen die Karte und die Belastung schlägt fehl |
| **Probezeit stillschweigend umgewandelt** | Unerwünschte Belastung auf Ihrem Kontoauszug | Das Limit oder die Sperrung stoppt es |
| **Kartendaten auf einem Forum verkauft** | Nutzbar für Betrug bei Karten-Non-Present | Nur bei einem Händler nutzbar, wenn überhaupt |

**Was sie nicht verändert, ist genauso wichtig.** Ihre Bank sieht die Transaktion weiterhin. Das Kartennetzwerk verarbeitet sie weiterhin. Der Herausgeber kennt weiterhin Ihre Identität, da Geldwäschegesetze eine Verifizierung verlangen. **Eine virtuelle Karte reduziert die Händlerseite-Exposition. Sie ist kein Weg, anonym zu bezahlen.**

*Diese Unterscheidung verwirrt ständig. Wenn Ihr Bedrohungsmodell den Herausgeber oder das Netzwerk einschließt, ändert eine virtuelle Karte daran nichts.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Diagramm zeigt eine virtuelle Kartennummer, die an den Händler geht, während die echte Kartennummer zwischen Karteninhaber und ausstellender Bank bleibt" >}}

## Die drei Arten von kartenförmigen Dingen

Die Terminologie wird uneinheitlich verwendet, und der Unterschied ist wichtig, wenn Sie entscheiden, was Sie einem Händler geben.

| Typ | Kartennummer | Physische Version | Typische Verwendung |
|---|---|---|---|
| **Digitale Karte** | Gleich wie Ihre physische Karte | Ja | Hinzufügen Ihrer bestehenden Karte zu einer mobilen Brieftasche |
| **Virtuelle Karte** | Anders als jede physische Karte | Nein | Online-Einkäufe, Abonnements, einmalige Händler |
| **Digital-first-Karte** | Anders, mit optional verknüpfter physischer Karte | Optional | Fintech-Konten, bei denen die physische Karte keine gedruckten Details trägt |

**Eine mobile Brieftasche verwendet einen ganz anderen Mechanismus.** Wenn Sie eine Karte zu einer Brieftasche hinzufügen, speichert die Brieftasche ein gerätespezifisches Token statt Ihrer PAN, und der Händler erhält das Token. Dies nennt man Tokenisierung und erklärt, warum das Bezahlen mit dem Telefon sicherer ist als das Übergeben der Plastikkarte, selbst ohne virtuelle Karte.

*Netzwerk-Tokenisierung und virtuelle Karten lösen sich überschneidende Teile desselben Problems. Tokenisierung schützt die Nummer während der Übertragung und im Ruhezustand. Eine virtuelle Karte schützt Sie vor dem, was der Händler danach behält.*

## Privacy.com Kartentypen

**Privacy.com bietet vier Kartenverhalten an, die nicht austauschbar sind.**

| Kartentyp | Verhalten | Am besten geeignet für |
|---|---|---|
| **Einmalige Nutzung** | Schließt automatisch nach einer Transaktion | Einmalkäufe und unbekannte Händler |
| **Händlergesperrt** | Sperrt auf den ersten Händler, der belastet, und schlägt anderswo fehl | Tägliches Online-Shopping |
| **Kategoriegesperrt** | Beschränkt auf eine Ausgabenkategorie | Begrenzung einer ganzen Ausgabeklasse |
| **Überall** | Eine physische Karte mit demselben Schutzmodell | Einkäufe vor Ort |

**Die Händlerbindung ist der Mechanismus mit dem größten Wert.** Eine gesperrte Karte schlägt bei jedem anderen Händler fehl als dem, bei dem sie zuerst verwendet wurde, was bedeutet, dass ein Datenleck beim Händler eine Nummer ergibt, die anderswo nutzlos ist.

**Einmalige Nutzung ist die stärkere Option, wo sie gilt.** Eine Karte, die nach einer Belastung schließt, kann überhaupt nicht wiederverwendet werden und erspart das spätere Schließen.

Zwei betriebliche Details, die es wert sind, bekannt zu sein:

- **Geteilte Karten sperren auf den ersten Händler, bei dem sie verwendet werden**, sodass das Teilen mit Familienmitgliedern oder Mitarbeitern die Händlersperre beibehält.
- **Eine Karte wird pausiert, nicht geschlossen.** Pausieren ist umkehrbar, was nützlich ist, wenn Sie ein Abonnement vorübergehend stoppen wollen, ohne die Kartendaten zu verlieren.

## Ausgabelimits und Kontrollen

**Jede Karte hat ein Ausgabelimit, das eine separate Kontrolle von der Händlersperre ist.**

| Kontrolle | Was sie verhindert |
|---|---|
| **Limit pro Transaktion** | Eine einzelne Belastung, die größer ist als von Ihnen autorisiert |
| **Monatliches Limit** | Aufgelaufene Belastungen über einen Abrechnungszeitraum |
| **Pause** | Jegliche Belastung, reversibel |
| **Schließen** | Jegliche zukünftige Belastung, dauerhaft |

**Setzen Sie sowohl ein Limit pro Transaktion als auch ein monatliches Limit auf jede Karte, die an ein Abonnement gebunden ist.** Eine stillschweigende Preiserhöhung des Händlers trifft das Limit statt Ihr Guthaben, und Sie bemerken es an einer fehlgeschlagenen Belastung statt an einer fehlenden Kontoauszugszeile.

*Unser **[Personal Finance Security](/personal-security-course/personal-finance/)**-Modul stellt dies neben Kredit-Sperren und Kartentokenisierung als die drei Kontrollen dar, die begrenzen, was ein einzelner kompromittierter Händler erreicht.*

## Pläne und was jeder freischaltet

Privacy.com bietet eine kostenlose Stufe neben drei kostenpflichtigen Plänen an. Preise und Leistungsgrenzen ändern sich, daher sollten Sie die aktuellen Bedingungen vor dem Abonnieren überprüfen.

| Plan | Preis | Bemerkenswerte Ergänzungen |
|---|---|---|
| **Persönlich (kostenlos)** | 0 $ | Virtuelle Karten, Händlerbindung, Ausgabenlimits, keine Gebühren bei Inlandszahlungen |
| **Plus** | 5 $/Monat | Kategorienkarten, Kartennotizen zur Ausgabenorganisation |
| **Pro** | 10 $/Monat | Cashback bei qualifizierten Einkäufen, physische Everywhere-Karten |
| **Premium** | 25 $/Monat | Alles aus Pro, mit monatlichem Kartenerstellungslimit auf 60 erhöht |

**Die kostenlose Stufe deckt den Kernvorteil der Sicherheit ab.** Händlerbindung, Einmalkarten und Ausgabenlimits sind die Mechanismen zur Reduzierung der Exposition und sind ohne Bezahlung verfügbar. Die kostenpflichtigen Stufen fügen Organisation und Komfort hinzu, nicht zusätzlichen Schutz.

**Auslandsgebühren unterscheiden sich je nach Stufe.** Die kostenlose Stufe berechnet 3 % auf Auslandszahlungen mit einem Mindestbetrag von 0,50 $, während die kostenpflichtigen Stufen keine Gebühren erheben.

## Was Privacy.com nicht leistet

**Klarheit über die Grenzen ist hilfreicher als eine Funktionsliste.**

| Einschränkung | Details |
|---|---|
| **Es macht Sie nicht anonym** | Ihre Identität wird bei der Anmeldung verifiziert und vom Aussteller gespeichert |
| **Es verbirgt die Transaktion nicht vor Ihrer Bank** | Ihre Bank sieht die Überweisung der Mittel, und das Netzwerk sieht die Belastung |
| **Es baut keine Kreditwürdigkeit auf** | Es handelt sich nicht um Kreditkonten, und es erfolgt keine Bonitätsprüfung |
| **Es ist nur für die USA verfügbar** | Erfordert US-Staatsbürgerschaft oder legalen Wohnsitz und ein US-Bank- oder Kreditgenossenschaftskonto |
| **Es erfordert Identitätsprüfung** | Know-Your-Customer-Prüfungen sind nach Geldwäschegesetzen verpflichtend |
| **Es deckt nicht jeden Händler ab** | Einige Händler blockieren Prepaid- und virtuelle Kartenbereiche |

**Der Punkt mit der Händlerblockade ist in der Praxis wichtig.** Einige Abonnementdienste und Fluggesellschaften lehnen Kartenbereiche ab, die sie mit virtuellen oder Prepaid-Karten assoziieren, und keine Konfiguration behebt das Problem. Halten Sie eine echte Karte als Backup für solche Fälle bereit.

*Die ehrliche Zusammenfassung: Eine virtuelle Karte ist eine Eindämmungsmaßnahme zur Begrenzung der Händlerexposition, kein Anonymitätswerkzeug. Wenn Sie Anonymität benötigen, ist das ein anderes Problem mit anderen Werkzeugen.*

## Wer die Karte ausgibt und warum das wichtig ist

**Eine virtuelle Karte ist trotzdem eine echte Karte, ausgegeben von einer echten Bank unter einer echten Schemalizenz.**

| Detail | Wert |
|---|---|
| **Ausgebende Bank** | Patriot Bank, N.A., Mitglied FDIC |
| **Schemalizenzen** | Mastercard und Visa |
| **Akzeptanzstellen** | Überall, wo Mastercard und Visa akzeptiert werden |
| **Finanzierung** | Überweisung von Ihrem verknüpften US-Girokonto |

**Deshalb ist der Schutz echt.** Die Karte bietet dieselben Schutzmechanismen wie jedes andere Mastercard- oder Visa-Produkt, was bedeutet, dass Rückbuchungsrechte und Betrugsstreitverfahren normal gelten. Es ist keine Geschenkkarte oder ein geschlossenes Guthaben.

Zwei Zertifizierungen sind erwähnenswert, da sie unabhängig überprüfbar sind und keine Marketingaussagen:

- **PCI-DSS-Konformität**, der Industriestandard für den Umgang mit Karteninhaberdaten
- **SOC 2 Typ II**, ein geprüfter Bericht über Sicherheitskontrollen über einen Zeitraum statt einer Momentaufnahme

**Zum Geschäftsmodell:** Das Unternehmen gibt an, Interchange-Gebühren von Händlern zu erhalten und keine Kundendaten an Werbetreibende oder Dritte zu verkaufen. Dies ist dasselbe Erlösmodell wie bei allen anderen Kartenausgebern und sollte als normal verstanden werden.

*Der praktische Grund, die ausgebende Bank zu prüfen, ist die Verifikation. Jeder kann behaupten, ein Kartenprogramm zu betreiben, und der Ausstellername auf der Karte ist das, was Sie mit der Bank im Papierkram abgleichen.*

Prüfen Sie das Schema und die Bank anhand des PAN-Präfixes mit dem **[Magnetic Stripe Decoder](/magnetic-stripe-decoder/)**, der den Hauptschemabereich meldet und die Luhn-Prüfziffer validiert.

## Virtuelle Karten richtig verwenden

**Die Kontrollen helfen nur, wenn Sie sie konfigurieren.** Sechs Gewohnheiten bringen den größten Nutzen.

1. **Sperren Sie jede Karte an einen Händler**, sofern kein Grund dagegen spricht. Die Sperre macht eine geleakte Nummer nutzlos.
2. **Verwenden Sie Einmalkarten für alles Unbekannte**, einschließlich Testversionen und Einzelkäufe bei kleineren Seiten.
3. **Setzen Sie beide Ausgabenlimits** bei Abonnementkarten, damit eine Preiserhöhung fehlschlägt statt belastet.
4. **Benennen Sie jede Karte nach dem Händler**, damit die Transaktionsliste lesbar ist und unerwartete Belastungen auffallen.
5. **Pausieren Sie statt zu schließen**, wenn Sie einen Dienst wieder aufnehmen wollen, und schließen Sie, wenn nicht.
6. **Halten Sie eine echte Karte für Händler bereit, die virtuelle Bereiche ablehnen**, damit eine blockierte Zahlung kein Notfall wird.

> **Häufiger Fehler: eine virtuelle Karte als Ersatz für das Überprüfen Ihrer Kontoauszüge zu sehen.** Händlerbindung verhindert eine Schadensart. Sie erkennt kein kompromittiertes Bankkonto, keine unautorisierte Überweisung oder betrügerische Belastung der dahinterliegenden echten Karte.

## Wichtige Erkenntnisse

- **Eine virtuelle Karte ändert die Nummer, die der Händler speichert.** Ihre echte PAN erreicht ihn nie, das ist der ganze Mechanismus.
- **Sie macht die Transaktion nicht privat.** Ihre Bank, das Netzwerk und der Aussteller sehen sie weiterhin, und Identitätsprüfung ist Pflicht.
- **Händlerbindung ist die wertvollste Funktion**, weil eine geleakte Nummer dann nirgendwo anders funktioniert.
- **Die kostenlose Stufe enthält die Sicherheitskontrollen.** Kostenpflichtige Pläne fügen Organisation und Komfort hinzu, keinen zusätzlichen Schutz.
- **Der Magnetstreifen speichert Kartendaten im Klartext** und wird bis 2033 abgeschafft, US-Banken stellen die Ausgabe 2027 ein.
- **Der CVV ist nicht auf dem Streifen**, weshalb ein Skimmer, der die Daten kopiert, nicht das hat, was viele Online-Händler verlangen.
- **Einige Händler lehnen virtuelle Kartenbereiche ab.** Halten Sie eine echte Karte als Backup bereit.
- **Verifizieren Sie die ausgebende Bank**, statt einer Kartenprogramm-Aussage zu vertrauen, und prüfen Sie das PAN-Präfix selbst.

## Nächste Schritte

1. **Untersuchen Sie die Track-Daten Ihrer eigenen Karte** und sehen Sie genau, was ein Magnetstreifen enthält: **[Magnetic Stripe Decoder and Encoder](/magnetic-stripe-decoder/)**
2. **Frieren Sie Ihre Kreditwürdigkeit ein**, falls noch nicht geschehen, da dies die stärkere Kontrolle gegen Betrug bei Neuanmeldungen ist: **[Personal Finance Security](/personal-security-course/personal-finance/)**
3. **Wenden Sie die Priorisierungsmethode an**, um zu entscheiden, wie viel Aufwand Ihre Situation erfordert: **[Prioritized Personal Security Checklist](/articles/personal-security-checklist-prioritized-2026/)**
4. **Überprüfen Sie die Pläne und aktuellen Bedingungen von Privacy.com**, bevor Sie ein Abonnement abschließen: **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Prüfen Sie, ob Ihre Daten bereits in einem Datenleck aufgetaucht sind**, bevor Sie davon ausgehen, dass Sie nicht betroffen sind: **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Lesen Sie die Checkliste zur Zahlungssicherheit** für die organisatorische Gegenpartei: **[Incident Response Checklist](/checklists/incident-response-checklist/)**

## Quellen

1. [Privacy.com – was virtuelle Karten sind, Händlerbindung und Ausgabenlimits](https://www.privacy.com/virtual-card)
2. [Digitale Karte – Wikipedia, behandelt digitale versus virtuelle Karten, Magnetstreifen-Tracks, Servicecodes, Parität und LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 – Identifikationskarten, Finanztransaktionskarten, Datenstruktur der Tracks 1 und 2](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 – detailliertes Layout der Track-Felder, einschließlich Sentinels und Servicecodes](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [PCI Security Standards Council – Anforderungen an die Umgebung für Karteninhaberdaten](https://www.pcisecuritystandards.org/)
6. [Consumer Financial Protection Bureau – Kreditberichte und Scores](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [ANSI/ISO ALPHA-Datenkodierung, der Zeichensatz und die Paritätstabelle für Track 1](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [ISO-Zeichen für Magnetkarten, die Track 1- und Track 2-Sets nebeneinander](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Magnetkartendaten lesen, eine praktische Anleitung mit einem Live-Kartenscan](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)
