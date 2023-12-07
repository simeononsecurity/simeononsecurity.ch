---
title: "Préchargement HSTS Comment améliorer la sécurité des sites web : Un guide étape par étape"
date: 2023-08-20
toc: true
draft: false
description: "Découvrez comment améliorer la sécurité des sites web et la confiance des utilisateurs en préchargeant les paramètres HSTS sur Chrome et Firefox. Suivez notre guide étape par étape pour une mise en œuvre transparente."
cover: "/img/cover/enhanced-website-security.png"
coverAlt: "Illustration de style bande dessinée d'un site web protégé par un cadenas, représentant une sécurité renforcée et une protection contre les cybermenaces."
coverCaption: "Renforcez la défense de votre site web, adoptez le préchargement HSTS."
---

## **Améliorer la sécurité des sites web avec le préchargement HSTS : Un guide étape par étape**

HTTP Strict Transport Security (HSTS) est un **mécanisme de sécurité crucial** qui garantit que les sites Web appliquent les connexions HTTPS afin de **protéger les utilisateurs contre les menaces de sécurité potentielles**. En préchargeant les paramètres HSTS sur Chrome et Firefox, vous pouvez **renforcer la sécurité des sites Web** et instaurer **la confiance des utilisateurs**. Dans ce guide complet, nous vous guiderons à travers les **étapes essentielles** pour précharger avec succès vos paramètres HSTS et nous vous fournirons des **recommandations utiles** pour optimiser la sécurité.

______

### **Comprendre le préchargement HSTS**

**Le préchargement HSTS** consiste à **soumettre le domaine de votre site web** aux listes de préchargement des principaux navigateurs. Une fois ajoutés, ces navigateurs **forceront automatiquement les connexions HTTPS** pour votre domaine et tous les sous-domaines. Cela garantit que les utilisateurs accèdent toujours à votre site web en toute sécurité, réduisant ainsi le risque d'attaques de type "homme du milieu" et d'écoutes non autorisées. Pour plus de détails sur le préchargement HSTS, vous pouvez vous référer au document officiel [documentation](https://hstspreload.org/)

______

______

### **Exigences de soumission**

Avant de soumettre votre domaine pour le préchargement HSTS, assurez-vous que votre site web répond aux **exigences essentielles** suivantes :

1. **Certificat valide** : Votre site web doit utiliser un **certificat SSL ou TLS valide** pour permettre des **connexions HTTPS sécurisées**.

2. Redirection **HTTP vers HTTPS** : Assurez-vous que toutes les requêtes **HTTP sont redirigées** vers leurs contreparties **HTTPS** lorsque votre site web écoute sur le port 80.

3. **HTTPS pour tous les sous-domaines** : Tous les sous-domaines de votre site web doivent **supporter les connexions HTTPS** pour être éligibles au préchargement HSTS.

4. **En-tête HSTS sur le domaine de base** : Incluez un **en-tête HSTS** sur votre domaine de base pour les requêtes HTTPS avec les paramètres suivants :
   - `max-age` doit être **au moins 31536000 secondes** (1 an).
   - Les `includeSubDomains` doit être spécifiée pour inclure tous les sous-domaines.
   - La directive `preload` doit être spécifiée pour demander l'inclusion dans la liste de préchargement.

Voici un exemple d'en-tête HSTS valide :

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

______

### **Comment précharger les paramètres HSTS**

Si votre site Web est **complètement engagé dans le HTTPS** et répond aux exigences ci-dessus, suivez ces **étapes cruciales** pour précharger avec succès vos paramètres HSTS :

1. **Examiner les sous-domaines** : Assurez-vous que tous les **sous-domaines de votre site web** fonctionnent correctement sur HTTPS afin d'offrir aux utilisateurs une expérience de navigation transparente.

2. **Mise en place progressive** : Pour tester et corriger tout problème potentiel, ajoutez l'en-tête **HSTS** à vos réponses HTTPS avec un niveau **faible**. `max-age` (par exemple, 300 secondes). Augmenter progressivement la valeur de `max-age` valeur par étapes :
   - 5 minutes : `max-age=300; includeSubDomains`
   - 1 semaine : `max-age=604800; includeSubDomains`
   - 1 mois : `max-age=2592000; includeSubDomains`

3. **Surveillez les indicateurs** : Au cours de chaque étape, **suivez de près les indicateurs** de votre site web, y compris le trafic et les revenus, afin d'identifier et de résoudre les problèmes éventuels avant de passer à l'étape suivante.

4. **Augmenter l'âge maximum à 2 ans** : Une fois que vous êtes **confiant qu'il n'y a plus de problèmes**, définissez la durée de vie maximale de votre site Web à 2 ans. `max-age` à **2 ans (63072000 secondes)** et ajoutez le `preload` à l'en-tête HSTS :
```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

5. **Soumettez votre site** : Après avoir mis en œuvre le programme de 2 ans `max-age` **soumettez votre site** à la liste de préchargement HSTS en utilisant le formulaire disponible sur [hstspreload.org](https://hstspreload.org/) Notez que l'inclusion dans la liste de préchargement peut prendre plusieurs mois avant d'atteindre les utilisateurs avec une mise à jour de Chrome.
______

### **Opt-In pour le préchargement HSTS : Donner du pouvoir aux opérateurs de sites**

La prise en charge du préchargement HSTS est une **excellente pratique de sécurité** qui améliore la protection des sites web. Cependant, il doit s'agir d'une décision **opt-in** pour les opérateurs de sites. Si vous fournissez des **conseils de configuration HTTPS** ou proposez une option pour activer HSTS, **évitez d'inclure l'option `preload` par défaut**. Cette approche permet d'éviter une inclusion involontaire dans la liste de préchargement, ce qui peut entraîner des difficultés d'accès à certains sous-domaines.

Pour garantir une expérience fluide, **informez les opérateurs de sites** des **conséquences à long terme** du préchargement et insistez sur **l'importance de satisfaire à toutes les exigences** avant d'activer HSTS pour leur domaine.

______

### **Removal from the Preload List : Une décision délibérée**

L'inclusion dans la liste de préchargement est une **décision permanente** qui ne peut pas être facilement annulée. Toutefois, si vous rencontrez de **fortes raisons techniques ou financières** empêchant la prise en charge HTTPS de certains sous-domaines, vous avez la possibilité de demander **la suppression de la liste de préchargement de Chrome** par l'intermédiaire de l'option [removal form](https://hstspreload.org/removal/)

Assurez-vous d'avoir soigneusement évalué les implications avant de prendre cette décision importante.
______

______

### **Une navigation plus sûre commence avec le préchargement HSTS**

En conclusion, le préchargement de vos paramètres HSTS sur Chrome et Firefox est une **étape proactive** vers une expérience de navigation web plus sûre pour vos utilisateurs. En **renforçant les connexions HTTPS**, vous **protégez les données sensibles** et instaurez **la confiance** parmi vos visiteurs. Suivez les **conseils** mentionnés ci-dessus pour **précharger vos paramètres HSTS** avec succès et profiter d'une **sécurité accrue sur votre site web**.

______

### Références

1. [Chromium - HTTP Strict Transport Security (HSTS)](https://www.chromium.org/hsts/)
2. [HSTS Preload Submission](https://hstspreload.org/)
3. [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
4. [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security/)
