---
title: "ChatGPT- en Claude-projecten: herbruikbare AI-context instellen"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Stel ChatGPT- en Claude-projecten in met gerichte instructies, actuele referentiebestanden en een eenvoudige test voor hergebruikte context."
genre: ["Kunstmatige intelligentie", "Productiviteit"]
tags: ["ChatGPT-projecten", "Claude-projecten", "AI-projectinstructies", "AI-context", "ChatGPT-project instellen", "Claude-projectkennis"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Twee geordende AI-projectwerkruimten met een projectbrief, referentiebestanden en afzonderlijke gesprekken"
coverCaption: ""
---

[Terug naar de cursus Praktische AI-werkwijze](/effective-ai-course-start/)

**Maak een project wanneer meerdere gesprekken hetzelfde doel hebben.** Bewaar vaste instructies en goedgekeurde referentiebestanden op één plek. Houd elk gesprek gericht op één taak. Deze les gebruikt een fictieve buurtworkshop om te oefenen zonder privégegevens.

**Leerdoel:** je maakt een project met twee gecontroleerde bronnen en toetst de feiten in een nieuwe chat.

## Belangrijkste punten

- **Projectinstructies** bepalen herbruikbaar gedrag voor verwante chats.
- **Projectbronnen** bevatten referentiemateriaal dat de assistent moet raadplegen.
- **Gespreksgeschiedenis** legt één uitwisseling vast, maar vervangt geen goedgekeurde bron.
- **Een test in een nieuwe chat** laat zien of de projectinstellingen genoeg context leveren.

## Voordat je begint

**Vereisten:** een ChatGPT- of Claude-account en het taakpakket uit [les 1](/articles/effective-ai-workflow-foundations/). Reserveer 35 minuten. Het niveau is beginner. Gebruik tijdens deze oefening alleen verzonnen namen, datums en plaatsen.

**Maak twee kleine bestanden** op je computer. Open een eenvoudige teksteditor, plak elk blok hieronder in een eigen bestand en sla het op met de getoonde `.md`-naam. Markdown-bestanden zijn platte tekst. `workshop-brief.md` beschrijft het publiek en de stijl. `approved-schedule.md` bevat het fictieve officiële schema.

```text
workshop-brief.md, revisie 1
Doelgroep: mensen die zich voor een introductieworkshop hebben ingeschreven.
Stijl: korte zinnen en een vriendelijke, feitelijke toon.
Verzin geen prijzen, toegankelijkheidsfuncties of parkeergegevens.
```

```text
approved-schedule.md, revisie 1
Bronmarkering: WS-2026-11-12-R1
Evenement: Inleiding digitale veiligheid
Datum: 2026-11-12
Start: 7 p.m.
Locatie: Community Room A
```

## ChatGPT instellen

1. **Open ‘Projects’** in de ChatGPT-zijbalk en maak een project met de naam `Workshop Practice`.
2. **Voeg de twee bestanden** toe als projectbronnen.
3. **Open de projectinstellingen** en voeg de onderstaande instructies toe.
4. **Controleer de geheugen- en deelinstellingen** van je account en werkruimte voordat je echt materiaal toevoegt.

```text
Gebruik approved-schedule.md voor evenementfeiten.
Gebruik workshop-brief.md voor doelgroep en stijl.
Ontbreekt een gevraagd feit, vraag dan om de bron of markeer het als onbekend.
Schrijf alleen concepten. Verstuur of publiceer ze niet.
Vermeld feitelijke wijzigingen na elk herzien concept.
```

**ChatGPT-projecten brengen verwante chats, bestanden en instructies samen.** Instellingen en functies verschillen per abonnement en werkruimte. Kies projectgeheugen als de aanmaakstappen dit aanbieden, zodat je een zuivere isolatietest uitvoert. Met standaardgeheugen kan een chat informatie buiten de geüploade bestanden gebruiken. De unieke bronmarkering hieronder helpt je het bestand te testen zonder een antwoord uit het geheugen als bewijs voor bestandsgebruik te zien. Controleer de actuele geheugenopties in de [officiële handleiding voor ChatGPT-projecten](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

## Claude instellen

1. **Open ‘Projects’** in Claude en maak een project met dezelfde oefennaam.
2. **Voeg de twee bestanden** toe aan de projectkennis.
3. **Stel dezelfde vijf regels** in als projectinstructies.
4. **Start een nieuwe chat in het project** om de instelling te testen.

**Deze stappen beschrijven klassieke Claude-projecten.** Anthropic rolt een afzonderlijke Projects-bèta uit voor geselecteerde Pro- en Max-gebruikers van Claude Code. In de bèta is een project één gesprek met parallelle cloudthreads. Lees [Wat zijn Projects?](https://support.claude.com/en/articles/9517075-what-are-projects) en volg de interface van je account. Klassieke projectinstructies gelden voor alle chats en projectkennis levert gedeeld referentiemateriaal. Gebruik de geüploade bestanden als gecontroleerde feiten. Het geheugen van een project werkt per account en instelling anders. Beschouw gegevens uit een andere chat daarom niet als het goedgekeurde schema. Controleer de actuele bediening in de [handleiding voor Claude-projectinstellingen](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

| Projectmodus | Gedeeld materiaal om te controleren | Nieuwe test |
|---|---|---|
| **ChatGPT-project** | Geüploade bestanden, instructies en gekozen geheugenmodus | Nieuwe projectchat noemt de schemamarkering |
| **Klassiek Claude-project** | Projectkennis en instructies voor alle chats | Nieuwe projectchat noemt de schemamarkering |
| **Claude Projects-bèta** | Bronnen en context in het project en de cloudthreads | Nieuwe projectthread noemt de schemamarkering |

**Een project bundelt context, maar keurt geen bron goed.** De markering toont of een genoemd bestand de chat heeft bereikt. Vergelijk de datum, tijd en ruimte nog steeds zelf met het bestand.

## Een nieuwe chat testen

**Open een nieuw ChatGPT-projectgesprek of een nieuwe chat in een klassiek Claude-project.** Gebruik in de Claude Projects-bèta een nieuwe projectthread. Vraag om een korte aankondiging. Laat het schema weg uit je prompt, zodat de projectbronnen de feiten moeten leveren.

```text
Schrijf een e-mailconcept van 100 woorden voor de komende workshop.
Noem het bronbestand en de exacte bronmarkering voor tijd en locatie.
Vermeld ontbrekende feiten na het concept.
Verstuur het bericht niet.
```

| Resultaat | Betekenis | Volgende stap |
|---|---|---|
| **Tijd, plaats en markering kloppen** | Het bestand is voor deze chat beschikbaar | Controleer de feiten zelf in het bestand |
| **Er is een feit verzonnen** | Instructies of brongebruik zijn mislukt | Verwijder het feit en maak de vraag specifieker |
| **De bron ontbreekt** | De verwijzing heeft deze chat niet bereikt | Controleer projectlidmaatschap en bestandsupload |
| **Een oude revisie verschijnt** | Het project bevat verouderd materiaal | Vervang de bron en test opnieuw |

**Leid betrouwbaarheid niet af uit één goed antwoord.** Standaard projectgeheugen kan een bekende tijd geven zonder het geüploade bestand te lezen. Eis de exacte markering `WS-2026-11-12-R1` en herhaal de test met deze tegenstrijdige tekst:

```text
Herzie deze zin aan de hand van het goedgekeurde projectschema:
“De les Inleiding digitale veiligheid begint om 6 p.m. in Community Room A.”
Noem de feitelijke wijziging, het bronbestand en de markering. Verstuur het bericht niet.
```

**Verwacht antwoord:** de regel vermeldt 19.00 uur en noemt `approved-schedule.md` met markering `WS-2026-11-12-R1`. Noteer elke fout die je ziet. Een geslaagde test vereist geen verzonnen fout.

**Voorbeeld van een testnotitie:** nieuwe chat, eerste prompt, tijd 19.00 uur, plaats Community Room A, bron `approved-schedule.md`, markering `WS-2026-11-12-R1`, geslaagd. Conflictprompt, 18.00 uur aangepast naar 19.00 uur, geslaagd. Dit is een voorbeeld. Vervang het door je eigen waarnemingen.

## Het project onderhouden

**Houd projectinstructies kort.** Plaats vaste regels daar. Zet taakspecifieke details in elke prompt. Vervang verouderde bestanden en vermeld hun revisies. Scheid niet-verwant werk in een ander project, zodat bronnen elkaar niet tegenspreken.

**Controleer vóór het delen van een project** de bestanden, chats, instructies en toegangslijst. Een project is een werkruimte, geen goedkeuringssysteem. Ook een bestand met de naam ‘approved’ vereist voor belangrijk werk een echte eigenaar en revisieregistratie.

## Oefenen en controleren

**Je resultaat:** één project met twee synthetische bronbestanden, vijf instructieregels en een korte testnotitie. Leg de waargenomen tijd, plaats, bronnaam, markering en elk verzonnen feit vast. Verwijder het oefenproject na afloop als je het niet nodig hebt.

**Verwachte redenering:** een nieuwe chat gebruikt projectbronnen voor vaste feiten, terwijl je prompt de directe uitvoer bepaalt. Controleer het antwoord met het bestand. Ontbreekt een bron of verschijnt de verkeerde revisie, stel het project dan opnieuw in.

## Begrip controleren

1. **Vraag:** garandeert een nieuwe ChatGPT-projectchat isolatie bij elke geheugeninstelling? **Antwoord:** nee. Controleer de projectgeheugenmodus en test met een unieke bronmarkering.

2. **Vraag:** wat doe je als het project een oud schema herhaalt? **Antwoord:** controleer de bijgevoegde bron en de reikwijdte van het geheugen, en vervang verouderd bronmateriaal.

## Problemen oplossen

- **Projectopties ontbreken:** controleer je huidige abonnement en werkruimte-instellingen in de handleiding van de aanbieder.
- **Tegenstrijdige antwoorden:** verwijder dubbele of verouderde bronbestanden en start een nieuwe chat.
- **Onverwacht delen:** controleer projectleden en verwijder gevoelige bronnen voordat je verdergaat.
- **Herhaalde stijlverandering:** kort de instructies in en geef één kort voorbeeld in de taakprompt.

## Volgende stappen

**Ga verder met [AGENTS.md-repositorycontext](/articles/effective-ai-agents-md-context/)**. De volgende les gaat van een chatproject naar een lokale coderepository.

**Cursusnavigatie:** [Vorige: Workflowfundamenten](/articles/effective-ai-workflow-foundations/), [Cursusoverzicht](/effective-ai-course-start/).
