---
title: "Bucle limitate pentru agenții AI: verificări, reîncercări și reguli de oprire"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Definește o buclă de obiectiv AI cu stare observabilă, verificări, limite pentru reîncercări, condiții de oprire și predare clară către o persoană."
genre: ["Inteligență artificială", "Inginerie software", "Productivitate"]
tags: ["bucle de obiectiv AI", "buclă de reîncercare a agentului", "reguli de oprire pentru automatizarea AI", "monitorizarea agenților", "predare umană pentru AI", "flux de lucru AI limitat"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "O buclă mică de agent trece de la o editare la un test, o decizie de reîncercare și predarea către o persoană"
coverCaption: ""
---

[Înapoi la cursul practic despre fluxuri de lucru AI](/effective-ai-course-start/)

**O buclă orientată spre un obiectiv repetă lucrul până când un rezultat definit trece o verificare sau se declanșează o regulă de oprire.** O buclă utilă citește starea curentă, execută o acțiune limitată, verifică rezultatul și înregistrează ce s-a întâmplat. O instrucțiune deschisă precum „continuă să încerci” nu are o regulă sigură de finalizare.

**Obiectiv de învățare:** vei rula o buclă de laborator limitată, cu o verificare despre care se știe că eșuează, și vei înregistra decizia de oprire.

## Idei principale

- **Obiectiv:** un rezultat descris în termeni observabili.
- **Stare:** fișierele, rezultatele, erorile și revizia sursei curente.
- **Verificare:** un test sau o evaluare legată de obiectiv.
- **Buget de reîncercări:** numărul maxim de încercări pentru o singură eroare.
- **Regulă de oprire:** o condiție care impune încheierea sau o decizie umană.

## Înainte să începi

**Cerințe preliminare:** [pachetul de sarcini](/articles/effective-ai-task-packets/), [registrul de verificare](/articles/effective-ai-output-verification/) și [lecția despre delegare](/articles/effective-ai-agent-delegation/). Rezervă 45 de minute. Dificultatea este intermediară. Folosește o copie nouă a laboratorului sintetic, astfel încât prima verificare eșuată să fie cunoscută dinainte.

## Scrie contractul buclei

**Pentru solicitarea de filtrare după stare**, stabilește contractul înainte de orice reîncercare:

```text
Obiectiv: suportă --status open|done fără a modifica ieșirea implicită.
Sursă: docs/requirements.md, revizia 1.
Fișiere permise: task_report.py și teste specifice.
Verificări: teste unitare, numărători 4/2/2, valoarea invalidă returnează un cod de ieșire diferit de zero.
Buget de reîncercări: cel mult două editări după prima încercare.
Oprește imediat: conflict în sursă, modificare neașteptată a unui fișier, divulgarea unui secret,
sau eșec de bază fără legătură cu această solicitare.
Predare: raportează diff-ul final, comenzile, rezultatele, încercările și problema nerezolvată.
```

**Bugetul este o regulă a sarcinii**, nu o setare implicită a produsului. Două reîncercări sunt suficiente pentru diagnosticarea unei sarcini mici de laborator fără a ascunde eșecurile repetate. O sarcină de producție are nevoie de o decizie proprie privind riscul și revizuirea.

## Folosește un tabel de stare

| Pas | Starea de înregistrat | Decizie |
|---|---|---|
| **Citește** | Revizia sursei și rezultatul inițial | Oprește-te dacă starea inițială diferă |
| **Acționează** | Fișiere modificate și acțiune efectuată | Respinge schimbările din afara domeniului |
| **Verifică** | Testul exact și rezultatul manual | Acceptă sau diagnostichează |
| **Reîncearcă** | Cauza erorii și o ipoteză nouă | Continuă numai în limita bugetului |
| **Predă** | Starea finală și următorul responsabil | Oprește-te după reușită sau blocaj |

**Înregistrează încercările, nu doar ultimul mesaj.** Un test care trece după trei editări ascunse nu explică ce s-a schimbat. Păstrează un jurnal scurt cu eroarea, ipoteza revizuită și dovezile noi.

## Analizează o eroare

**Exemplu de primă încercare:** agentul adaugă filtrarea și testele. `open` afișează 2, dar `--status invalid` afișează 0 și se încheie cu succes. Cerința spune că o valoare nevalidă trebuie să returneze un cod de ieșire diferit de zero. Marchează verificarea drept eșuată.

**Diagnostic:** inspectează validarea argumentelor. Agentul a tratat o valoare necunoscută ca pe o potrivire goală, în loc să o considere eroare. Solicită o corecție limitată care validează valorile acceptate înainte de numărare. Rulează din nou cazul nevalid și toate verificările anterioare.

```text
Încercarea 1: starea invalidă a returnat succes, deci criteriul de acceptare a eșuat.
Cauză găsită: valorile acceptate nu sunt validate.
Solicitarea pentru încercarea 2: respinge valorile neacceptate și păstrează numărătorile 4/2/2.
Dovezi necesare: rularea completă a testelor și codul de ieșire al comenzii invalide.
```

**Rezultatul așteptat la a doua încercare:** o eroare clară și un cod de ieșire diferit de zero pentru `invalid`, cu numărătorile valide neschimbate. Dacă a doua încercare eșuează în continuare, folosește ultima reîncercare numai după identificarea unei cauze noi. Repetarea aceleiași solicitări nu este diagnosticare.

## Gestionează rezultatele ambigue

**Un proces care se oprește fără rezultat nu a reușit.** Dacă un instrument expiră după o posibilă scriere, inspectează fișierele și starea Git înainte de a-l rula din nou. Dacă un serviciu conectat raportează un rezultat necunoscut, citește starea curentă înainte de a repeta o acțiune externă. În afara laboratorului, trimiterile, publicările sau scrierile duplicate reprezintă un risc real.

**Oprește-te pentru o revizuire umană** dacă cerința intră în conflict cu o altă sursă aprobată, o permisiune blochează acțiunea, bugetul de reîncercări s-a epuizat sau acțiunea solicitată depășește o limită de publicare. Predarea trebuie să precizeze starea exactă și decizia rămasă.

## Separă buclele de monitoare

**O buclă de editare** rulează în cadrul unei sarcini limitate și verifică rezultatul după fiecare acțiune. **Un monitor programat** se activează mai târziu pentru a inspecta o condiție. Un monitor are nevoie de propria frecvență, un prag de schimbare, o regulă de notificare și o condiție de oprire. Nu transforma bucla de editare din laborator într-o sarcină recurentă. Lecția următoare evaluează sistemele persistente înainte de activare.

## Rulează o buclă controlată

**Începe cu laboratorul neatins.** Cele două teste inițiale trec. În copia nouă, creează `tests/test_loop_contract.py` cu verificarea de mai jos. Acest fișier descrie o funcție dorită care lipsește din proiectul inițial. Nu face parte din arhiva ZIP inițială, menținută.

```python
"""One controlled failing check for the status-filter exercise."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LoopContractTests(unittest.TestCase):
    def test_open_status_count(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"),
             str(ROOT / "tasks.json"), "--status", "open"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Total tasks: 2")


if __name__ == "__main__":
    unittest.main()
```

**Rulează `python3 -m unittest discover -s tests -v`.** Cele două teste originale ar trebui să treacă, iar noul test de contract ar trebui să eșueze deoarece proiectul inițial nu acceptă `--status`. Înregistrează eșecul real. Dacă ai inițializat Git conform lecției 0, înregistrează și `git status --short`. În caz contrar, compară fișierele modificate cu o copie neatinsă. Pe Windows, folosește `py -3` dacă configurația folosește launcherul.

**Stabilește un buget de trei încercări:** prima editare și cel mult două corecții. Oferă agentului contractul buclei de mai sus și cere o singură editare limitată. După fiecare încercare, inspectează fișierele modificate, rulează din nou toate testele și execută comenzile implicite, `open`, `done` și valoarea nevalidă. Înregistrează cauza eșecului înainte de o nouă încercare. Oprește-te după o reușită, un eșec de bază fără legătură cu solicitarea, o modificare în afara domeniului sau al treilea eșec.

**Traseu de studiu:** după ce înregistrezi testul roșu, aplică [răspunsul complet pentru lecția 5](/articles/effective-ai-coding-agent-first-task/) în această copie nouă. Rulează din nou aceleași verificări și notează că editarea agentului nu a fost executată. Păstrează testul de contract controlat. Nu îl slăbi și nu îl șterge ca să treacă.

| Încercare | Stare și observație | Decizie |
|---|---|---|
| **Înainte de editare** | Cele două teste inițiale trec, noua verificare `open` eșuează | Continuă cu o editare limitată |
| **După fiecare editare** | Înregistrează testele exacte, numărătorile, codul de ieșire pentru valoarea nevalidă și fișierele modificate | Acceptă, diagnostichează sau oprește-te |
| **La epuizarea bugetului** | Înregistrează eroarea rămasă și diferența curentă | Predă fără altă încercare |

## Exersează și verifică

**Artefactul tău:** testul controlat care eșuează, rezultatele observate înainte și după, un jurnal al încercărilor și o decizie finală de acceptare sau oprire. Dacă prima editare reușește, înregistrează o singură încercare. Nu inventa o a doua eroare ca să umpli jurnalul.

**Verificare de finalizare:** contractul indică o sursă, domeniul fișierelor, verificări observabile, limita de reîncercări, cel puțin o condiție imediată de oprire și o predare. Jurnalul include testul roșu real, rezultatele verificărilor ulterioare și fie reușita, fie oprirea din cauza bugetului. A doua încercare indică o cauză nouă și diferă de prima.

## Verifică ce ai înțeles

1. **Întrebare:** ce demonstrează primul test de contract roșu? **Răspuns:** proiectului inițial îi lipsește filtrul de stare solicitat, lucru demonstrat de un test scris înainte de editare.
2. **Întrebare:** când trebuie să se oprească bucla chiar dacă mai sunt încercări? **Răspuns:** la o modificare în afara domeniului, o permisiune neclară sau o cerință contradictorie.

## Depanare

- **Bucla repetă aceeași eroare:** oprește-te și formulează o ipoteză nouă despre cauză.
- **Verificările devin mai slabe:** restaurează criteriile originale de acceptare.
- **Rezultat extern incert:** inspectează starea curentă înainte de o altă încercare.
- **Buget epuizat:** predă jurnalul erorilor în loc să le ascunzi.

## Pașii următori

Continuă cu [Evaluarea agenților specializați](/articles/effective-ai-specialized-agent-evaluation/), lecție opțională, sau treci direct la [proiectul final al cursului despre fluxuri de lucru AI](/articles/effective-ai-capstone/). Pentru alte opțiuni de runtime, consultă [ghidul mediilor pentru agenți](/articles/best-ai-agent-harnesses/).

**Navigarea cursului:** [Anterioară: Delegarea agenților](/articles/effective-ai-agent-delegation/), [Programa cursului](/effective-ai-course-start/).
