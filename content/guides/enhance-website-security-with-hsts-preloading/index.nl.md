---
title: "HSTS Preloading Hoe de beveiliging van websites te verbeteren: Een stap-voor-stap handleiding"
date: 2023-08-20
toc: true
draft: false
description: "Leer hoe u de beveiliging van websites en het vertrouwen van gebruikers kunt verbeteren door HSTS-instellingen vooraf te laden in Chrome en Firefox. Volg onze stapsgewijze handleiding voor naadloze implementatie."
cover: "/img/cover/enhanced-website-security.png"
coverAlt: "Een illustratie in cartoonstijl van een website afgeschermd met een slot, wat staat voor verbeterde beveiliging en bescherming tegen cyberbedreigingen."
coverCaption: "Versterk de verdediging van je website, omarm HSTS preloading."
---

**Verbeteren van websitebeveiliging met HSTS Preloading: Een stap-voor-stap handleiding**

HTTP Strict Transport Security (HSTS) is een **cruciaal beveiligingsmechanisme** dat ervoor zorgt dat websites HTTPS-verbindingen afdwingen om **gebruikers te beschermen tegen potentiële beveiligingsrisico's**. Door HSTS-instellingen vooraf in te stellen in Chrome en Firefox, kunt u de beveiliging van websites verbeteren en het vertrouwen van gebruikers opbouwen. In deze uitgebreide handleiding doorlopen we de **essentiële stappen** om uw HSTS-instellingen met succes vooraf te laden en geven we **gebruikelijke aanbevelingen** om de beveiliging te optimaliseren.

______

**Uitleg over het vooraf laden van HSTS**

**HSTS Preloading** is het proces waarbij het domein van uw website** wordt toegevoegd aan de voorlaadlijsten van de belangrijkste browsers. Eenmaal toegevoegd, zullen deze browsers **automatisch HTTPS-verbindingen** afdwingen voor uw domein en alle subdomeinen. Dit zorgt ervoor dat gebruikers altijd veilig toegang hebben tot uw website en vermindert het risico op **man-in-the-middle aanvallen** en onbevoegd afluisteren. Voor meer informatie over HSTS preloading kunt u de officiële [documentation](https://hstspreload.org/)

______

{{< inarticle-dark >}}

______

**Inzendvereisten**

Voordat u uw domein voor HSTS pre-loading indient, moet u ervoor zorgen dat uw website voldoet aan de volgende **essentiële vereisten**:

1. **Geldig certificaat**: Uw website moet een **geldig SSL- of TLS-certificaat** hebben om **veilige HTTPS-verbindingen** mogelijk te maken.

2. **HTTP naar HTTPS omleiding**: Zorg ervoor dat alle **HTTP verzoeken worden omgeleid** naar hun **HTTPS tegenhangers** wanneer uw website luistert op poort 80.

3. **HTTPS voor alle subdomeinen**: Alle subdomeinen van je website moeten ** HTTPS-verbindingen** ondersteunen om in aanmerking te komen voor HSTS preloading.

4. **HSTS header op basisdomein**: Neem een **HSTS header** op uw basisdomein op voor HTTPS verzoeken met de volgende instellingen:
   - `max-age` moet **minimaal 31536000 seconden** (1 jaar) zijn.
   - De `includeSubDomains` moet worden opgegeven om alle subdomeinen op te nemen.
   - De `preload` directive moet worden opgegeven om opname in de preloadlijst aan te vragen.

Hier is een voorbeeld van een geldige HSTS-header:

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

______

**Hoe HSTS instellingen vooraf laden**

Als uw website **geheel overgaat op HTTPS** en voldoet aan de bovenstaande eisen, volg dan deze **cruciale stappen** om uw HSTS-instellingen met succes vooraf te laden:

1. **Onderzoek subdomeinen**: Zorg ervoor dat alle **subdomeinen van uw website** correct werken via HTTPS om gebruikers een naadloze browse-ervaring te bieden.

2. **Geleidelijk opvoeren**: Om mogelijke problemen te testen en op te lossen, voegt u de **HSTS header** toe aan uw HTTPS-reacties met een **lage `max-age` waarde** (bijvoorbeeld 300 seconden). Verhoog geleidelijk de `max-age` waarde in stappen:
   - 5 minuten: `max-age=300; includeSubDomains`
   - 1 week: `max-age=604800; includeSubDomains`
   - 1 maand: `max-age=2592000; includeSubDomains`

3. **Monitor statistieken**: Houd tijdens elke fase de statistieken van uw website** nauwlettend in de gaten, waaronder verkeer en omzet, om eventuele problemen te identificeren en aan te pakken voordat u doorgaat naar de volgende fase.

4. **Verhoog de maximale leeftijd naar 2 jaar**: Zodra u **verzekerd bent dat er geen problemen meer zijn**, stelt u de `max-age` naar **2 jaar (63072000 seconden)** en voeg de `preload` richtlijn naar de HSTS-header:
```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

5. **Stuur uw site in**: Na het implementeren van de 2-jarige `max-age` instelling, **submit your site** to the HSTS preload list using the form available on [hstspreload.org](https://hstspreload.org/) Merk op dat het enkele maanden kan duren voordat gebruikers met een Chrome-update worden opgenomen in de preloadlijst.
______

**Opt-In voor HSTS Preloading: Sitebeheerders in staat stellen**

Het ondersteunen van HSTS preloading is een **uitstekende beveiligingspraktijk** die de bescherming van websites verbetert. Het moet echter een **opt-in beslissing** zijn voor sitebeheerders. Als u **HTTPS configuratieadvies** geeft of een optie aanbiedt om HSTS in te schakelen, **vermijd dan het opnemen van de `preload` richtlijn standaard**. Deze aanpak voorkomt onbedoelde opname in de preloadlijst, wat kan leiden tot problemen bij het benaderen van bepaalde subdomeinen.

Om een soepele ervaring te garanderen, **informeer websitebeheerders** over de **langetermijngevolgen** van preloading en benadruk het **belang van het voldoen aan alle vereisten** voordat HSTS voor hun domein wordt ingeschakeld.

______

**Verwijdering van de voorlaadlijst: Een bewuste beslissing**

Opname in de preloadlijst is een **permanente beslissing** die niet gemakkelijk ongedaan kan worden gemaakt. Als u echter **sterke technische of kostengerelateerde redenen** tegenkomt waardoor HTTPS-ondersteuning voor bepaalde subdomeinen niet mogelijk is, hebt u de optie om **verwijdering van de voorlaadlijst** van Chrome** aan te vragen via de optie [removal form](https://hstspreload.org/removal/)

Zorg ervoor dat je de implicaties zorgvuldig hebt geëvalueerd voordat je deze belangrijke beslissing neemt.
______

{{< inarticle-dark >}}

______

**Veiliger browsen begint met HSTS vooraf laden**

Concluderend, het vooraf laden van uw HSTS-instellingen in Chrome en Firefox is een **proactieve stap** naar een veiligere surfervaring voor uw gebruikers. Door **het versterken van HTTPS-verbindingen**, **beschermt u gevoelige gegevens** en bouwt u **vertrouwen** op bij uw bezoekers. Volg de bovenstaande **richtlijnen** om **met succes uw HSTS instellingen** te **preloaden** en geniet van **verhoogde websitebeveiliging**.

______

### Referenties

1. [Chromium - HTTP Strict Transport Security (HSTS)](https://www.chromium.org/hsts/)
2. [HSTS Preload Submission](https://hstspreload.org/)
3. [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
4. [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security/)
