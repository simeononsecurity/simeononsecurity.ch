---
title: "Um guia para autenticação multifator: tipos e práticas recomendadas"
date: 2023-03-02
toc: true
draft: false
description: "Aprenda sobre os diferentes tipos de autenticação multifator e como escolher o melhor para suas necessidades de segurança em nosso guia definitivo."
tags: ["autenticação multifator", "segurança online", "senha de segurança", "fatores de autenticação", "autenticação de dois fatores", "fichas de hardware", "autenticação de software", "cíber segurança", "ataques de phishing", "prevenção de hackers", "Proteção de dados", "Verificação de Identidade", "senha de segurança", "tokens de segurança", "controle de acesso", "roubo de identidade", "ameaças cibernéticas", "segurança digital", "aplicativos de autenticação", "defesa cibernética"]
cover: "/img/cover/A_cartoon_person_standing_in_front_of_a_computer.png"
coverAlt: "Uma pessoa de desenho animado em frente a um computador, com um símbolo de cadeado acima da cabeça e diferentes tipos de fatores de autenticação, como chave, telefone, impressão digital etc., flutuando ao seu redor"
coverCaption: ""
---

Com o aumento das violações de segurança online, tornou-se necessário usar mais do que apenas uma senha para proteger o acesso a informações confidenciais. É aí que entra a **autenticação multifator**, que fornece uma camada adicional de segurança ao exigir que os usuários forneçam dois ou mais fatores de autenticação para obter acesso às suas contas.

## Os diferentes tipos de fatores no MFA

Existem vários tipos de fatores de autenticação usados na autenticação multifator:

- **Algo que você sabe:** inclui informações que apenas o usuário conhece, como senha, PIN ou resposta a uma pergunta de segurança. Um exemplo disso é fazer login em uma conta de mídia social usando uma senha.

- **Algo que você tem:** inclui um objeto físico que apenas o usuário possui, como uma chave USB, cartão inteligente ou telefone celular. Um exemplo disso é usar um cartão inteligente para acessar uma instalação segura do governo.

- **Algo que você é:** inclui informações biométricas, como impressões digitais, reconhecimento facial ou varreduras de íris. Um exemplo disso é desbloquear um smartphone usando o reconhecimento facial.

- **Em algum lugar onde você está:** inclui informações baseadas em localização, como a localização GPS ou o endereço IP do usuário. Um exemplo disso é um banco que exige que um usuário autentique sua localização antes de permitir o acesso à sua conta.

- **Algo que você faz:** inclui biometria comportamental, como velocidade de digitação do usuário, movimentos do mouse ou padrões de fala. Um exemplo disso é um sistema que pode reconhecer a maneira como um usuário digita para autenticar sua identidade.

Usar vários fatores para autenticar a identidade de um usuário é mais seguro do que usar um único fator, como uma senha. Ao usar uma combinação de fatores de autenticação, torna-se muito mais difícil para os invasores obter acesso não autorizado a informações confidenciais.

### Os prós e contras de cada fator no MFA

Aqui estão os prós e contras de cada tipo de autenticação multifator (MFA):

- **Algo que você sabe:**

  - Prós: Fácil de usar, pode ser alterado com frequência e pode ser compartilhado com várias pessoas (como uma senha de equipe).
  
  - Contras: pode ser comprometido por phishing, adivinhação ou ataques de força bruta e pode ser esquecido ou perdido.

- **Algo que você tem:**

  - Prós: Difícil de copiar ou roubar, pode ser usado offline e pode ser facilmente substituído em caso de perda ou roubo.
  
  - Contras: pode ser esquecido ou perdido, pode ser roubado se não estiver devidamente protegido e pode ser caro para implementar.

- **Algo que você é:**

  - Prós: Único para cada indivíduo, difícil de forjar e não pode ser perdido ou esquecido.
  
  - Contras: pode ser afetado por mudanças na aparência do usuário, pode ser difícil de implementar para grandes grupos de usuários e pode ser visto como invasivo.

- **Em algum lugar você está:**

  - Prós: pode fornecer contexto adicional para autenticação, como garantir que o usuário esteja na localização geográfica correta.
  
  - Contras: pode ser falsificado usando redes privadas virtuais (VPNs) ou servidores proxy, pode ser impreciso ou impreciso e pode ser difícil de implementar para usuários móveis.

- **Algo que você faz:**

  - Prós: Difícil de duplicar, pode ser usado para identificar indivíduos específicos e não pode ser perdido ou esquecido.
  
  - Contras: pode ser afetado por lesões ou deficiências, pode exigir hardware ou software especializado e pode não ser eficaz para todos os usuários.
  
Embora a autenticação baseada em hardware, como o uso de um token físico como o YubiKey da Yubico, seja considerada a mais segura, a autenticação baseada em SMS e a autenticação baseada em e-mail são consideradas os métodos menos seguros, pois são vulneráveis a interceptação e falsificação.

### Melhor método de autenticação multifator para segurança

Embora todos os tipos de autenticação multifator ofereçam mais segurança do que usar apenas uma senha, alguns métodos são mais seguros do que outros. Autenticação baseada em hardware, como usar um token físico como o [Yubico's YubiKey](https://amzn.to/3kPk1wy) or the [OnlyKey](https://amzn.to/3Zi5SXM) são considerados os mais seguros, pois exigem a posse física do token, geram um código exclusivo para cada tentativa de login e não são suscetíveis a ataques de phishing ou hacking.

A autenticação baseada em SMS e a autenticação baseada em e-mail são consideradas os métodos menos seguros, pois são vulneráveis a interceptação e falsificação.

### Um bom método de compromisso entre segurança e facilidade de uso

A geração de token 2FA baseada em software é um bom compromisso entre facilidade de uso e segurança. Em vez de depender de tokens físicos de hardware, os tokens 2FA baseados em software são gerados por um aplicativo no smartphone ou computador do usuário.

Esses aplicativos geralmente geram um código exclusivo para cada tentativa de login, fornecendo uma camada adicional de segurança além de apenas uma senha. Esse tipo de 2FA é mais seguro do que a autenticação baseada em SMS e a autenticação baseada em e-mail, que são vulneráveis a interceptação e falsificação.

Os tokens 2FA baseados em software têm a capacidade de fazer backup com mais facilidade do que os tokens de hardware, o que pode ser um pró e um contra. Por um lado, isso significa que os usuários podem transferir mais facilmente seu 2FA para um novo dispositivo se perderem o antigo, tornando mais conveniente para eles acessarem suas contas.

No entanto, isso também significa que, se alguém obtiver acesso ao código de backup de um usuário, poderá obter acesso a todas as suas contas que usam esse token 2FA. Como tal, é importante que os usuários mantenham seus códigos de backup em um local seguro, como um gerenciador de senhas ou uma unidade criptografada.
______

## Tipos de autenticação multifator

Existem vários tipos de métodos de autenticação multifator disponíveis, cada um usando diferentes combinações dos fatores de autenticação:

- **Autenticação de dois fatores (2FA):** Este é o tipo mais comum de autenticação multifator e exige que os usuários forneçam dois fatores de autenticação diferentes, como uma senha e um código de verificação enviado por SMS.

- **Autenticação de três fatores (3FA):** exige que os usuários forneçam três fatores de autenticação diferentes, como senha, leitura de impressão digital e cartão inteligente.

- **Autenticação de quatro fatores (4FA):** esse é o tipo mais seguro de autenticação multifator e exige que os usuários forneçam quatro fatores de autenticação diferentes, como senha, leitura de impressão digital, cartão inteligente e reconhecimento facial Varredura.

______

## Vale a pena usar mais de dois fatores?

A decisão de usar mais de dois fatores na autenticação multifator depende, em última análise, do nível de segurança necessário para a conta. Para a maioria das contas, a autenticação de dois fatores é suficiente. No entanto, para contas altamente confidenciais, como aquelas que contêm informações financeiras ou médicas, o uso de mais de dois fatores, como uma combinação de algo que você conhece, algo que você tem e algo que você é, pode fornecer uma camada extra de segurança.

______

## Problemas com tokens de hardware

Embora a autenticação baseada em hardware seja considerada o método mais seguro de autenticação multifator, há problemas com o uso de tokens de hardware. Para garantir a segurança máxima, você deve usar apenas um token de hardware para todas as suas contas e mantê-lo em um local seguro que apenas algumas pessoas conheçam. Além disso, se você ficar gravemente doente ou falecer, seus entes queridos podem não conseguir acessar suas contas se você tiver apenas um token de hardware.

Como backup, é recomendável usar um método de autenticação secundário, como um aplicativo de autenticação baseado em software, para garantir que você possa acessar suas contas se perder ou extraviar seu token de hardware. No entanto, isso não é aconselhável em todas as situações. E cabe a você determinar o que é prioridade. Segurança ou Convivência.

## Conclusão

No mundo digital de hoje, a necessidade de medidas robustas de segurança online tornou-se mais importante do que nunca. A autenticação multifator é um componente crítico da segurança online, fornecendo uma camada adicional de proteção que torna muito mais difícil para os invasores obter acesso não autorizado a informações confidenciais.

Ao exigir que os usuários forneçam vários fatores de autenticação, como algo que sabem, algo que possuem ou algo que são, o MFA ajuda a evitar métodos de ataque comuns, como phishing, ataques de força bruta e adivinhação de senha. Embora a autenticação baseada em hardware seja considerada o método mais seguro, os tokens 2FA baseados em software oferecem um bom equilíbrio entre segurança e facilidade de uso.

Por fim, a decisão de usar mais de dois fatores na MFA depende do nível de segurança necessário para a conta. Para a maioria das contas, a autenticação de dois fatores é suficiente, mas para contas altamente confidenciais, o uso de mais de dois fatores pode fornecer uma camada extra de segurança.

Concluindo, a implementação da autenticação multifator é uma etapa importante para proteger suas contas online e proteger informações confidenciais contra ameaças cibernéticas.

## Referências

- [NIST Special Publication 800-63B: Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
- [Yubico's - Authentication standards](https://www.yubico.com/authentication-standards/)
- [Microsoft's - Multifactor authentication in Azure AD ](https://www.microsoft.com/en-us/security/business/identity-access/azure-active-directory-mfa-multi-factor-authentication)
- [Google's Guide to Two-Factor Authentication](https://www.google.com/landing/2step/)
- [Okta's - Setting Up and Authenticating with Multi-factor Authentication (MFA)](https://support.okta.com/help/s/end-user-adoption-toolkit/setting-up-mfa-for-end-users?language=en_US)
