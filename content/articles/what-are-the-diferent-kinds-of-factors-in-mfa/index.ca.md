---
title: "Una guia per a l'autenticació multifactor: tipus i bones pràctiques"
date: 2023-03-02
toc: true
draft: false
description: "Obteniu informació sobre els diferents tipus d'autenticació multifactor i com triar la millor per a les vostres necessitats de seguretat a la nostra guia definitiva."
tags: ["autenticació multifactor", "seguretat en línia", "seguretat de contrasenya", "factors d'autenticació", "autenticació de dos factors", "fitxes de maquinari", "autenticació de programari", "seguretat cibernètica", "atacs de pesca", "prevenció de la pirateria", "protecció de dades", "verificació d'identitat", "seguretat de contrasenya", "fitxes de seguretat", "control d'accés", "el robatori d'identitat", "ciberamenaces", "seguretat digital", "aplicacions d'autenticació", "ciberdefensa"]
cover: "/img/cover/A_cartoon_person_standing_in_front_of_a_computer.png"
coverAlt: "Una persona de dibuixos animats davant d'un ordinador, amb un símbol de pany a sobre del seu cap i diferents tipus de factors d'autenticació, com ara una clau, un telèfon, una empremta digital, etc., flotant al seu voltant"
coverCaption: ""
---

Amb l'augment de les infraccions de seguretat en línia, s'ha fet necessari utilitzar més que una contrasenya per assegurar l'accés a la informació sensible. Aquí és on entra l'**autenticació multifactor**, que proporciona una capa addicional de seguretat en requerir als usuaris que proporcionin dos o més factors d'autenticació per accedir als seus comptes.

## Els diferents tipus de factors a l'MFA

Hi ha diversos tipus de factors d'autenticació utilitzats en l'autenticació multifactor:

- **Alguna cosa que saps:** inclou informació que només coneix l'usuari, com ara una contrasenya, un PIN o una resposta a una pregunta de seguretat. Un exemple d'això és iniciar sessió a un compte de xarxes socials amb una contrasenya.

- **Alguna cosa que tens:** Inclou un objecte físic que només posseeix l'usuari, com ara una clau USB, una targeta intel·ligent o un telèfon mòbil. Un exemple d'això és l'ús d'una targeta intel·ligent per accedir a una instal·lació governamental segura.

- **Alguna cosa que ets:** Inclou informació biomètrica, com ara empremtes dactilars, reconeixement facial o exploracions de l'iris. Un exemple d'això és desbloquejar un telèfon intel·ligent mitjançant el reconeixement facial.

- **En algun lloc on et trobes:** Inclou informació basada en la ubicació, com ara la ubicació GPS o l'adreça IP de l'usuari. Un exemple d'això és un banc que requereix que un usuari autentiqui la seva ubicació abans de permetre l'accés al seu compte.

- **Alguna cosa que feu:** inclou dades biometriques del comportament, com ara la velocitat d'escriptura de l'usuari, els moviments del ratolí o els patrons de parla. Un exemple d'això és un sistema que pot reconèixer la manera com escriu un usuari per autenticar la seva identitat.

Utilitzar diversos factors per autenticar la identitat d'un usuari és més segur que utilitzar un sol factor, com ara una contrasenya. En utilitzar una combinació de factors d'autenticació, és molt més difícil que els atacants tinguin accés no autoritzat a informació sensible.

### Els avantatges i els contres de cada factor en MFA

Aquests són els avantatges i els contres de cada tipus d'autenticació multifactor (MFA):

- **Alguna cosa que saps:**

  - Avantatges: fàcil d'utilitzar, es pot canviar amb freqüència i es pot compartir amb diverses persones (com ara una contrasenya d'equip).
  
  - Contres: es pot veure compromesa per phishing, endevinar o atacs de força bruta, i es pot oblidar o perdre.

- **Alguna cosa que tens:**

  - Avantatges: és difícil de copiar o robar, es pot utilitzar fora de línia i es pot substituir fàcilment si es perd o es roba.
  
  - Contres: es pot oblidar o perdre, es pot robar si no està ben assegurat i pot ser car d'implementar.

- **Alguna cosa que ets:**

  - Avantatges: únic per a cada individu, difícil de forjar i no es pot perdre ni oblidar.
  
  - Contres: es pot veure afectat pels canvis en l'aparença de l'usuari, pot ser difícil d'implementar per a grans grups d'usuaris i es pot veure com a invasiu.

- ** En algun lloc ets:**

  - Avantatges: pot proporcionar un context addicional per a l'autenticació, com ara assegurar-se que l'usuari es troba a la ubicació geogràfica correcta.
  
  - Contres: es pot falsificar mitjançant xarxes privades virtuals (VPN) o servidors intermediaris, pot ser inexacte o imprecís i pot ser difícil d'implementar per als usuaris mòbils.

- **Alguna cosa que fas:**

  - Avantatges: és difícil de duplicar, es pot utilitzar per identificar individus específics i no es pot perdre ni oblidar.
  
  - Contres: pot ser afectat per lesions o discapacitat, pot requerir maquinari o programari especialitzat i pot ser que no sigui efectiu per a tots els usuaris.
  
Si bé l'autenticació basada en maquinari, com l'ús d'un testimoni físic com YubiKey de Yubico, es considera la més segura, l'autenticació basada en SMS i l'autenticació basada en correu electrònic es consideren els mètodes menys segurs, ja que són vulnerables a la intercepció i la falsificació.

### Millor mètode d'autenticació multifactor per a la seguretat

Tot i que tots els tipus d'autenticació multifactor ofereixen una millor seguretat que utilitzar només una contrasenya, alguns mètodes són més segurs que d'altres. Autenticació basada en maquinari, com ara l'ús d'un testimoni físic com el [Yubico's YubiKey](https://amzn.to/3kPk1wy) or the [OnlyKey](https://amzn.to/3Zi5SXM) es consideren els més segurs, ja que requereixen la possessió física del testimoni, generen un codi únic per a cada intent d'inici de sessió i no són susceptibles a atacs de phishing o pirateria informàtica.

L'autenticació basada en SMS i l'autenticació basada en correu electrònic es consideren els mètodes menys segurs, ja que són vulnerables a la intercepció i la falsificació.

### Un bon mètode de compromís entre la seguretat i la facilitat d'ús

La generació de testimonis 2FA basada en programari és un bon compromís entre la facilitat d'ús i la seguretat. En lloc de confiar en fitxes de maquinari físic, els testimonis 2FA basats en programari es generen mitjançant una aplicació al telèfon intel·ligent o a l'ordinador de l'usuari.

Aquestes aplicacions solen generar un codi únic per a cada intent d'inici de sessió, proporcionant una capa addicional de seguretat més enllà d'una contrasenya. Aquest tipus de 2FA és més segur que l'autenticació basada en SMS i l'autenticació basada en correu electrònic, que són vulnerables a la intercepció i la falsificació.

Els fitxes 2FA basats en programari tenen la capacitat de fer una còpia de seguretat més fàcilment que els fitxes de maquinari, que poden ser tant un pro com un contra. D'una banda, això vol dir que els usuaris poden transferir més fàcilment el seu 2FA a un nou dispositiu si perden el seu antic, cosa que fa que sigui més còmode per a ells accedir als seus comptes.

Tanmateix, això també significa que si algú accedeix al codi de còpia de seguretat d'un usuari, pot tenir accés a tots els seus comptes que utilitzen aquest testimoni 2FA. Per tant, és important que els usuaris guardin els seus codis de seguretat en una ubicació segura, com ara un gestor de contrasenyes o una unitat xifrada.
______

## Tipus d'autenticació multifactor

Hi ha diversos tipus de mètodes d'autenticació multifactorial disponibles, cadascun utilitza diferents combinacions dels factors d'autenticació:

- **Autenticació de dos factors (2FA):** Aquest és el tipus més comú d'autenticació multifactor i requereix que els usuaris proporcionin dos factors d'autenticació diferents, com ara una contrasenya i un codi de verificació enviat per SMS.

- **Autenticació de tres factors (3FA):** Això requereix que els usuaris proporcionin tres factors d'autenticació diferents, com ara una contrasenya, una exploració d'empremtes digitals i una targeta intel·ligent.

- **Autenticació de quatre factors (4FA):** aquest és el tipus d'autenticació multifactor més segur i requereix que els usuaris proporcionin quatre factors d'autenticació diferents, com ara una contrasenya, una exploració d'empremtes digitals, una targeta intel·ligent i un facial. escanejar.

______

## Val la pena utilitzar més de dos factors?

La decisió d'utilitzar més de dos factors en l'autenticació multifactorial depèn en última instància del nivell de seguretat necessari per al compte. Per a la majoria de comptes, l'autenticació de dos factors és suficient. Tanmateix, per als comptes molt sensibles, com els que contenen informació financera o mèdica, l'ús de més de dos factors, com ara una combinació d'alguna cosa que coneixeu, quelcom que teniu i quelcom que sou, pot proporcionar una capa addicional de seguretat.

______

## Problemes amb fitxes de maquinari

Tot i que l'autenticació basada en maquinari es considera el mètode més segur d'autenticació multifactor, hi ha problemes amb l'ús de fitxes de maquinari. Per garantir la màxima seguretat, només hauríeu d'utilitzar un testimoni de maquinari per a tots els vostres comptes i mantenir-lo en una ubicació segura que només coneixen poques persones. A més, si alguna vegada et poses greument malalt o mors, és possible que els teus éssers estimats no puguin accedir als teus comptes si només tens un testimoni de maquinari.

Com a còpia de seguretat, es recomana que utilitzeu un mètode d'autenticació secundari, com ara una aplicació d'autenticació basada en programari, per assegurar-vos que podeu accedir als vostres comptes si perdeu o perdeu el testimoni de maquinari. No obstant això, això no és aconsellable en totes les situacions. I depèn de vosaltres decidir què és una prioritat. Seguretat o convivència.

## Conclusió

En el món digital actual, la necessitat de mesures de seguretat en línia sòlides ha esdevingut més important que mai. L'autenticació multifactor és un component crític de la seguretat en línia, ja que proporciona una capa addicional de protecció que fa que sigui molt més difícil que els atacants tinguin accés no autoritzat a informació sensible.

En exigir als usuaris que proporcionin diversos factors d'autenticació, com ara alguna cosa que saben, alguna cosa que tenen o alguna cosa que són, l'MFA ajuda a prevenir mètodes d'atac habituals, com ara la pesca, els atacs de força bruta i l'endevinació de contrasenyes. Tot i que l'autenticació basada en maquinari es considera el mètode més segur, els testimonis 2FA basats en programari ofereixen un bon equilibri entre seguretat i facilitat d'ús.

En definitiva, la decisió d'utilitzar més de dos factors a MFA depèn del nivell de seguretat necessari per al compte. Per a la majoria de comptes, l'autenticació de dos factors és suficient, però per als comptes molt sensibles, l'ús de més de dos factors pot proporcionar una capa addicional de seguretat.

En conclusió, la implementació de l'autenticació multifactorial és un pas important per protegir els vostres comptes en línia i protegir la informació sensible de les amenaces cibernètiques.

## Referències

- [NIST Special Publication 800-63B: Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
- [Yubico's - Authentication standards](https://www.yubico.com/authentication-standards/)
- [Microsoft's - Multifactor authentication in Azure AD ](https://www.microsoft.com/en-us/security/business/identity-access/azure-active-directory-mfa-multi-factor-authentication)
- [Google's Guide to Two-Factor Authentication](https://www.google.com/landing/2step/)
- [Okta's - Setting Up and Authenticating with Multi-factor Authentication (MFA)](https://support.okta.com/help/s/end-user-adoption-toolkit/setting-up-mfa-for-end-users?language=en_US)
