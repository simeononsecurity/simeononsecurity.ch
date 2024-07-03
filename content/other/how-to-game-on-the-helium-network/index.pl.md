---
title: "Gra w sieci Helium: Wykorzystywanie luk w zabezpieczeniach za pomocą MiddleMan i multipleksera pakietów Chirp Stack"
date: 2023-02-18
toc: true
draft: false
description: "Dowiedz się, jak wykorzystać luki w sieci Helium za pomocą MiddleMan i Chirp Stack Packet Multiplexer, a także jakie są zagrożenia i konsekwencje takiego działania."
tags: ["Sieć helowa", "Proof-of-Coverage", "MiddleMan", "Multiplekser pakietów Chirp Stack", "gaming", "wykorzystywanie słabych punktów", "Sieć LoRaWAN", "kryptowaluta", "blockchain", "sieć zdecentralizowana", "hotspoty", "spoofing", "oszukiwanie", "nielegalna działalność", "kary", "integralność sieci", "nagrody", "złośliwi aktorzy", "bezpieczeństwo sieci", "legalne hosty"]
cover: "/img/cover/A_cartoonish_depiction_of_a_group_of_individuals_exploiting.png"
coverAlt: "Karykaturalne przedstawienie grupy osób wykorzystujących balon z helem z wizerunkiem bramki LoRaWAN i multipleksera pakietów MiddleMan lub Chirp Stack w tle."
coverCaption: ""
---

**Disclaimer**:
Należy zauważyć, że hazard w sieci Helium jest bezprawną i nieetyczną działalnością, która jest zdecydowanie nieakceptowana przez społeczność Helium i szerszą społeczność kryptowalut i blockchain. Granie w sieci podważa integralność sieci i szkodzi legalnym gospodarzom, którzy zapewniają cenny zasięg sieci.

Ponadto, chociaż wykorzystanie MiddleMan i Chirp Stack Packet Multiplexer do wykorzystania luk w sieci Helium może być powodem do niepokoju, należy zauważyć, że te problemy mogą zostać naprawione przez Helium tylko poprzez wprowadzenie bezpiecznych bram. Wymagałoby to wymiany wszystkich hotspotów w sieci, co jest znaczącym przedsięwzięciem i może być niewykonalne. W związku z tym społeczność Helium musi zachować czujność i proaktywność w rozwiązywaniu problemów związanych z grami w sieci.

Warto również zauważyć, że zespół Helium jest świadomy problemu od pewnego czasu i podjął kroki w celu jego rozwiązania, ale wymagane są dalsze działania, aby rozwiązać problem. Społeczność wzywa do podjęcia rzeczywistych działań w celu wyeliminowania tych luk i zapewnienia, że sieć może nadal skalować się i rozwijać w bezpieczny i godny zaufania sposób.

Pisząc ten artykuł, mamy nadzieję zwiększyć świadomość na temat problemu gier w sieci Helium oraz wykorzystania MiddleMan i Chirp Stack Packet Multiplexer do wykorzystania luk w systemie. Wierzymy, że rzucając światło na tę kwestię i nadając jej większy rozgłos, społeczność Helium oraz szersza społeczność blockchain i kryptowalut może zjednoczyć się w celu rozwiązania problemu i pracy nad bardziej bezpieczną i godną zaufania siecią.

Ponadto, podkreślając ten problem, mamy nadzieję zachęcić zespół Helium do podjęcia bardziej zdecydowanych działań w zakresie usuwania luk w sieci i wdrożenia solidniejszych środków bezpieczeństwa, aby zapobiec grom w przyszłości. Uważamy, że ważne jest, aby zespół Helium był przejrzysty w swoich wysiłkach zmierzających do rozwiązania tego problemu i aby informował społeczność o swoich postępach w usuwaniu tych luk.

Mamy nadzieję, że dzięki nagłośnieniu tej sprawy, uda nam się zwiększyć świadomość i edukację na temat ryzyka i konsekwencji gier w sieci Helium. Ważne jest, aby użytkownicy rozumieli znaczenie etycznego zachowania w sieci oraz potencjalne szkody, które mogą być spowodowane przez gry. Dzięki wspólnej pracy nad tymi kwestiami możemy zapewnić stały rozwój i sukces sieci Helium.

Podsumowując, hazard w sieci Helium nie jest akceptowany ani przez społeczność, ani przez nas, dlatego zachęcamy użytkowników do etycznego i legalnego działania w sieci. Chociaż w sieci istnieją luki, które mogą zostać wykorzystane, ważne jest, aby zachować czujność i proaktywność w rozwiązywaniu tych problemów i pracować nad bardziej bezpieczną i niezawodną siecią dla wszystkich użytkowników.

## Jak oszukać sieć Helium za pomocą MiddleMana i multipleksera pakietów Chirp Stack
Sieć Helium jest zdecentralizowaną siecią LoRaWAN®, która wynagradza tych, którzy są gospodarzami fizycznych hotspotów, nagradzając ich tokenami Helium, czyli $HNT. System ten znany jest jako Proof-of-Coverage (PoC). Wraz z rozwojem sieci i wzrostem świadomości tego projektu, pojawiła się coraz większa liczba oszustów, którzy wykorzystują protokół i mechanizmy nagradzania. W tym artykule omówimy, jak grać w sieci Helium przy użyciu MiddleMan i Chirp Stack Packet Multiplexer.

## Zrozumienie problemu hazardu w sieci Helium
Sieć Helium opiera się na systemie Proof-of-Coverage, aby zapewnić, że hotspoty zapewniają zasięg tam, gdzie jest on potrzebny. Jednak system ten jest podatny na gry, spoofing, hacking i inne rodzaje złego zachowania, które mogą zaszkodzić sieci. Problem z grami w sieci Helium kosztuje legalnych hostów tysiące dolarów miesięcznie. Helium, Inc, wraz z DeWi, podjęło na początku 2022 roku agresywne działania, aby pomóc wykorzenić ten problem.

## Wymagany sprzęt.
-[Dragino LPS8](https://www.ebay.com/sch/i.html?_nkw=dragino+lps8)
-[Other Lorawan Gateways that Use the Semtech Forwarder](https://amzn.to/41bcskb)
-[Raspberry Pi](https://amzn.to/3KjFCYp)
-[Other PC that can run docker images or linux software](https://amzn.to/3YkFhcj)

## Używanie MiddleMana do gry w sieci Helium
Jednym ze sposobów na oszukanie sieci Helium jest użycie MiddleMana. MiddleMan to oprogramowanie, które może być wykorzystane do stworzenia fałszywego hotspotu, który wydaje się zapewniać zasięg w określonej lokalizacji. Za pomocą MiddleMana użytkownik może stworzyć fałszywy hotspot, który będzie otrzymywał nagrody za zapewnienie zasięgu na danym obszarze, mimo że fizycznie nie znajduje się on na tym obszarze.

Aby skorzystać z MiddleMan, użytkownik musi zainstalować oprogramowanie i stworzyć fałszywy hotspot. Następnie użytkownik może skonfigurować hotspot, aby zgłaszał swoją lokalizację do sieci Helium za pomocą narzędzia do spoofingu GPS. Sieć Helium uwierzy, że fałszywy hotspot zapewnia zasięg w podanej lokalizacji i nagrodzi użytkownika kwotą $HNT.

Skonfigurowałbyś swoją bramkę lorawan tak, aby wskazywała na to oprogramowanie, a ono manipuluje wartościami tak, aby wszystkie otrzymane PoC były uznane za ważne.  Używanie semtech forwarder jest jednym z różnych standardów w społeczności LoraWAN. Naprawa problemu manipulacji wymagałaby ponownego wynalezienia koła i wdrożenia własnego protalu od podstaw. Rzeczy takie jak sumy kontrolne i szyfrowanie uniemożliwiłyby to. Ale utrudniłoby to również sprzedawcom z innym sprzętem tworzenie hotspotów. Nie wspominając o tym, że jest to obsługiwany przypadek użycia, aby mieć jeden górnik helu i wiele bramek lora dla lepszego zasięgu. Chociaż jest to bardziej problem na poziomie przedsiębiorstwa.

 -[helium-DIY-middleman](https://github.com/curiousfokker/helium-DIY-middleman)

## Używanie multipleksera pakietów Chirp Stack do gry w sieci Helium
Innym sposobem na grę w sieci Helium jest użycie Chirp Stack Packet Multiplexer. Chirp Stack Packet Multiplexer jest narzędziem, które może być użyte do stworzenia wirtualnego hotspotu, który może odbierać pakiety z wielu fizycznych hotspotów. Używając Chirp Stack Packet Multiplexer, użytkownik może stworzyć wirtualny hotspot, który będzie odbierał pakiety z fizycznych hotspotów w wielu lokalizacjach, co zwiększy zdobywane nagrody.

Aby użyć Chirp Stack Packet Multiplexer, użytkownik musi zainstalować oprogramowanie i skonfigurować je tak, aby odbierało pakiety z fizycznych hotspotów lub bramek lorawan w wielu lokalizacjach. Hotspot będzie odbierał pakiety i zgłaszał swoją lokalizację do sieci Helium, która nagrodzi użytkownika kwotą $HNT.

Pozwala to na korzystanie z wielu forwarderów na wejściu i wielu bramek na wyjściu. Istnieją uzasadnione przypadki użycia tego oprogramowania w społeczności LoraWAN, ale używanie go w helu jest w najlepszym wypadku szarą strefą. To zależy od tego, jak go używasz, a także od tego, jaki jest twój zamiar.

Konfiguracja tego wymaga kilku plików konfiguracyjnych. Ale można to zrobić w 5 minut lub mniej.
-[chirpstack-packet-multiplexer](https://github.com/brocaar/chirpstack-packet-multiplexer)


## Ryzyko i konsekwencje gry w sieci Helium
Granie w sieci Helium jest ryzykownym i nielegalnym działaniem, które może mieć poważne konsekwencje. Helium, Inc. oraz DeWi aktywnie pracują nad wykrywaniem i zapobieganiem grom w sieci, a użytkownicy, którzy zostaną przyłapani na grywaniu w sieci, będą karani.

Kary za grę w sieci Helium mogą obejmować utratę dostępu do sieci, permanentny zakaz korzystania z hotspotów oraz utratę wszystkich $HNT, które zostały zarobione w wyniku gry. Ponadto, hazard w sieci Helium podważa integralność sieci i szkodzi legalnym hostom, którzy zapewniają cenny zasięg sieci.

## Wniosek
Podczas gdy sieć Helium zapewnia legalnym hostom hotspotów możliwość zarabiania poprzez Proof-of-Coverage, stanowi ona również atrakcyjny cel dla złośliwych aktorów chcących grać w systemie. Użycie MiddleMana i Chirp Stack Packet Multiplexer, choć nie jest popierane przez Helium Inc. ani przez szerszą społeczność, jest przykładem tego, jak niektórzy źli aktorzy wykorzystują luki w sieci, aby czerpać korzyści kosztem innych.

Ważne jest, aby społeczność Helium kontynuowała współpracę w celu zidentyfikowania i rozwiązania problemu gier w sieci, ponieważ zagrażają one integralności systemu i podważają wysiłki legalnych hostów. Może to obejmować wysiłki mające na celu opracowanie i wdrożenie bardziej zaawansowanych środków wykrywania i zapobiegania, jak również zwiększenie świadomości i edukacji na temat ryzyka i konsekwencji gier w sieci.

W ostatecznym rozrachunku sukces sieci Helium zależy od gotowości jej uczestników do współpracy w celu zbudowania bezpiecznego, niezawodnego i godnego zaufania systemu, który będzie stanowił prawdziwą wartość dla jego użytkowników. Dzięki czujności i proaktywności w rozwiązywaniu problemów związanych z grami, społeczność może pomóc w zapewnieniu, że sieć Helium będzie się nadal rozwijać i ewoluować w pozytywnym kierunku.