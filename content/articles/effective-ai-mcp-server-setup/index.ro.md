---
title: "Configurarea unui server MCP: permisiuni, testarea instrumentelor și eliminarea sigură"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Conectați un server MCP de documentație doar pentru citire, inspectați instrumentele, efectuați o citire reală și eliminați conexiunea."
genre: ["Inteligență artificială", "Instrumente pentru dezvoltatori"]
tags: ["Configurare server MCP", "Protocolul contextului modelelor (MCP)", "Permisiuni MCP", "MCP în Codex", "MCP în Claude Code", "MCP în OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Un client IA conectat la un server de documentație doar pentru citire, cu instrumentul și limita de acces vizibile"
coverCaption: ""
---

[Înapoi la cursul Flux de lucru practic cu IA](/effective-ai-course-start/)

**Folosiți un server MCP când o sarcină necesită un instrument reutilizabil sau informații actualizate din afara proiectului.** Model Context Protocol, sau MCP, definește schimbul de informații despre instrumente, resurse și prompturi dintre client și server. O intrare de server nu dovedește că instrumentul funcționează. Lecția testează o conexiune la documentație, doar pentru citire.

**Obiectiv de învățare:** veți deosebi configurarea de o citire MCP reală și veți documenta eliminarea în siguranță.

## Idei principale

- **Gazdă MCP:** aplicația IA care coordonează utilizatorii, modelele, permisiunile și clienții.
- **Client MCP:** componenta protocolului care comunică cu un server.
- **Server MCP:** program sau serviciu la distanță care oferă instrumente, resurse ori prompturi.
- **Descoperirea instrumentului:** dovada că în client apare o funcție cu nume.
- **Executarea instrumentului:** dovada unui apel real și a conținutului returnat.
- **Domeniul permisiunilor:** accesul acordat de gazdă, server, cont și utilizator.

## Înainte de a începe

**Cerințe preliminare:** [exercițiu de context și predare a lucrului](/articles/effective-ai-context-window-management/) și o instalare actuală de Codex CLI pentru traseul explicat. Rezervați 35 de minute. Dificultate medie. Ceilalți agenți de programare au ghiduri de configurare separate. [Serverul oficial OpenAI Docs MCP](https://learn.chatgpt.com/learn/docs-mcp) oferă documentație pentru dezvoltatori, doar pentru citire, și nu solicită încărcarea datelor cursului.

**Folosiți laboratorul sintetic al cursului.** Nu conectați calendarul, e-mailul sau un sistem de producție pentru acest exercițiu. Citirea documentației este suficientă pentru a înțelege stările conexiunii.

## Înțelegeți limitele

| Stare | Ce dovedește | Ce nu dovedește |
|---|---|---|
| **Configurat** | Există o intrare de server | Accesibilitatea |
| **Conectat** | Clientul a ajuns la server | Existența unor instrumente utile |
| **Descoperit** | Apare un instrument numit | Reușita apelului său |
| **Executat** | Un apel a returnat conținut | Corectitudinea sarcinii finale |
| **Verificat** | Sursa și rezultatul răspund la întrebare | Reușita tuturor apelurilor viitoare |

**MCP nu acordă singur permisiuni pentru cont.** Contează gazda clientului, serverul, autentificarea, domeniul contului și setările locale de aprobare. [Specificația MCP](https://modelcontextprotocol.io/specification/2026-07-28) definește protocolul, iar fiecare produs își controlează propria interfață.

**Tratați rezultatul serverului ca material-sursă.** O pagină preluată nu înlocuiește sarcina și nu autorizează scrierea fișierelor. Fiecare definiție de instrument consumă și context. Conectați numai serverul necesar acestei citiri și eliminați-l după exercițiu.

## Conectarea documentației pentru citire

**În Codex CLI,** rulați aceste comenzi într-un terminal. Prima adaugă serverul public de documentație, iar a doua listează serverele configurate.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Dovada de configurare așteptată:** lista conține `openaiDeveloperDocs`. Aceasta dovedește numai înregistrarea. Porniți o sesiune Codex nouă în directorul laboratorului extras și inspectați instrumentele MCP cu `/mcp`. Folosiți numele afișate de versiunea instalată.

**Cereți o citire reală:**

```text
Folosiți serverul MCP al documentației pentru dezvoltatorii OpenAI ca să găsiți îndrumările actuale AGENTS.md.
Indicați titlul și URL-ul paginii-sursă, două puncte relevante pentru laborator și instrumentul MCP folosit.
Nu editați fișiere.
```
**Inspectați rezultatul.** Pagina returnată trebuie să descrie `AGENTS.md` drept îndrumări ale depozitului și să includă URL-ul exact al sursei. Deschideți pagina citată și confirmați subiectul. Un răspuns fără apel MCP în transcriere este un răspuns obișnuit, nu dovada executării instrumentului.

## Diagnosticați o problemă

**Dacă `codex mcp list` afișează serverul, dar `/mcp` nu afișează instrumente,** înregistrarea a reușit, iar descoperirea a eșuat. Reporniți sesiunea, verificați serverele active cu `/mcp` și configurația salvată cu `codex mcp get openaiDeveloperDocs`, apoi controlați URL-ul serverului și accesul la rețea. Nu declarați configurarea MCP reușită doar pe baza intrării.

**Dacă apare un instrument, dar citirea eșuează,** notați eroarea și reîncercați o dată după verificarea conectivității. Dacă același apel eșuează din nou, folosiți pagina oficială citată în browser drept sursă alternativă și marcați exercițiul MCP ca incomplet. Nu inventați rezultatul unui instrument.

## Eliminați conexiunea

**După citire,** eliminați serverul de practică din Codex CLI și confirmați dispariția intrării.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Dovada eliminării așteptată:** `openaiDeveloperDocs` lipsește din lista nouă. Reporniți o sesiune Codex activă înainte să verificați dacă instrumentele disponibile s-au schimbat. Eliminarea definiției locale nu revocă o autorizare separată a contului folosită de alt serviciu.

## Folosiți o aplicație diferită

**Claude Code și OpenCode acceptă și ele MCP.** Urmați [ghidul MCP pentru Claude Code](https://code.claude.com/docs/en/mcp) sau [ghidul MCP pentru OpenCode](https://opencode.ai/docs/mcp-servers/) potrivit versiunii instalate. Înregistrați aceleași cinci stări: configurat, conectat, descoperit, executat și verificat. Schema de configurare OpenCode și permisiunile agenților diferă între versiuni. Folosiți exemplele din ghidul potrivit instalării.

**Pentru un traseu exclusiv în browser,** citiți [pagina oficială AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) și completați aceeași fișă de verificare. Marcați descoperirea și executarea instrumentelor ca „neefectuate”. Traseul exersează verificarea surselor, dar nu dovedește funcționarea MCP.

## Exersați și verificați

**Rezultatul dvs.:** un registru de conexiune cu cinci rânduri: numele serverului, numele instrumentului, URL-ul sursei, rezultatul observat și dovada eliminării. Nu includeți tokenuri sau identificatori de cont în capturi și jurnale.

**Criteriu de finalizare:** traseul conectat este promovat numai după o citire reală cu instrumentul și eliminarea ulterioară a configurației. Traseul de rezervă finalizează verificarea sursei cu MCP marcat drept neexecutat.

## Verificați-vă înțelegerea

1. **Întrebare:** o intrare MCP salvată dovedește că instrumentul a funcționat? **Răspuns:** nu. Verificați descoperirea, permisiunile și o citire reală.
2. **Întrebare:** ce cost de context adaugă o conexiune MCP extinsă? **Răspuns:** descrierile și schemele instrumentelor consumă o parte din contextul activ.

## Depanare

- **Comanda `codex` nu este recunoscută:** instalați sau actualizați Codex CLI din ghidul oficial asociat.
- **Serverul apare, dar nu există instrument:** inspectați starea sesiunii și diagnosticele serverului.
- **Apelul a returnat conținut irelevant:** restrângeți solicitarea și verificați pagina-sursă.
- **Eliminarea pare ineficientă:** porniți o sesiune nouă și inspectați lista serverelor active.

## Pașii următori

**Continuați cu [Verificarea rezultatelor IA](/articles/effective-ai-output-verification/).** Pentru extensii mai ample, citiți [ghidul site-ului despre pluginurile Claude Code și instrumentele MCP](/articles/claude-code-plugins-skills-mcp-tools/).

**Navigarea cursului:** [Anterior: Gestionarea contextului](/articles/effective-ai-context-window-management/), [Planul cursului](/effective-ai-course-start/).
