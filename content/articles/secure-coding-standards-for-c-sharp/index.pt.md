---
title: "Padrões de codificação segura para desenvolvedores C#"
date: 2023-02-28
lastmod: 2026-11-19
toc: true
draft: false
description: "Aprenda boas práticas de codificação segura em C# para reduzir o risco de incidentes de segurança e proteger dados sensíveis."
tags: ["codificação segura", "desenvolvimento em C#", "programação em C#", "práticas de codificação segura", "segurança em C#", "segurança do ASP.NET", "segurança do .NET Core", "validação de entrada", "hash de senhas", "criptografia", "princípio do menor privilégio", "analisador estático de código", "segurança de aplicações web", "prevenção de injeção de SQL", "prevenção de script entre sites", "proteção de dados", "verificações de integridade", "gerenciamento de sessão", "boas práticas da OWASP", "padrões de codificação segura em C#", "diretrizes de segurança para C#", "dicas de codificação segura", "desenvolvimento seguro de software", "estruturas de software de codificação segura", "técnicas de codificação segura", "recomendações de codificação segura", "programação segura em C#", "vulnerabilidades de codificação segura", "ferramentas de codificação segura", "tutoriais de codificação segura", "boas práticas de codificação segura em C#", "diretrizes de codificação segura para C#", "padrões de codificação segura para desenvolvedores C#", "práticas de codificação segura em C#", "como implementar codificação segura em C#", "dicas de codificação segura para programadores C#", "codificação segura em aplicações web C#", "estruturas de software de codificação segura em C#", "técnicas de codificação segura para desenvolvedores C#", "ferramentas de codificação segura em C#"]
cover: "/img/cover/A_cartoon_developer_with_a_lock_icon_as_the_head_surrounded.webp"
coverAlt: "Ilustração de um desenvolvedor de desenho animado com um ícone de cadeado no lugar da cabeça, cercado por código e protegido por um firewall."
coverCaption: ""
---

A codificação segura ajuda a manter o código confiável e livre de vulnerabilidades. C# é uma linguagem de programação popular, e os desenvolvedores precisam seguir padrões de codificação segura para reduzir riscos. Validar entradas, evitar funções inseguras, usar bibliotecas de criptografia e manter bibliotecas e estruturas de software atualizados são boas práticas.

_____

## Validação de entrada

As entradas dos usuários podem ser uma fonte importante de riscos de segurança. A validação verifica se a entrada atende aos critérios esperados e se é segura para uso na aplicação. Por exemplo, um número de cartão de crédito deve conter apenas dígitos, sem caracteres especiais. Os desenvolvedores podem usar classes integradas, como `Regex`, para verificar os critérios.

```csharp
public static bool ValidateInput(string inputString)
{
    bool isValid = false;
    // Verifique se a cadeia de entrada contém somente dígitos
    if (Regex.IsMatch(inputString, @"^\d+$"))
    {
        isValid = true;
    }
    return isValid;
}
```

Esse método usa expressões regulares para verificar se a cadeia de entrada contém somente dígitos. Ele retorna um valor booleano que indica se a entrada é válida.

## Evite usar funções inseguras

Algumas funções de C# podem criar problemas de segurança quando usadas sem cuidado. `Process.Start()`, `Reflection` e `Deserialization` podem permitir que invasores executem código malicioso. Evite essas funções ou use-as com cautela, restringindo os parâmetros de entrada e recorrendo a elas apenas quando necessário.

Para iniciar um processo externo, use `Process.StartInfo` para especificar argumentos e restrições de segurança, em vez de chamar `Process.Start()` diretamente.

```csharp
ProcessStartInfo startInfo = new ProcessStartInfo
{
    FileName = "notepad.exe",
    Arguments = "example.txt",
    UseShellExecute = false,
    RedirectStandardOutput = true,
    CreateNoWindow = true
};

using (Process process = new Process())
{
    process.StartInfo = startInfo;
    process.Start();
    string output = process.StandardOutput.ReadToEnd();
    process.WaitForExit();
}
```

## Use bibliotecas de criptografia

Bibliotecas como Bouncy Castle e as APIs de criptografia do .NET Framework oferecem meios seguros de criptografar e descriptografar dados. Use essas bibliotecas em vez de criar métodos de criptografia próprios, que podem conter vulnerabilidades.

Por exemplo, para derivar um valor a partir de uma senha, use a classe `Rfc2898DeriveBytes` das APIs de criptografia do .NET Framework:

```csharp
public static string EncryptPassword(string password)
{
    byte[] salt = new byte[16];
    using (var rng = new RNGCryptoServiceProvider())
    {
        rng.GetBytes(salt);
    }

    var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 10000);
    byte[] hash = pbkdf2.GetBytes(20);

    byte[] hashBytes = new byte[36];
    Array.Copy(salt, 0, hashBytes, 0, 16);
    Array.Copy(hash, 0, hashBytes, 16, 20);

    return Convert.ToBase64String(hashBytes);
}
```

A classe `Rfc2898DeriveBytes` gera um sal e o usa para derivar uma chave da senha. Essa chave é então usada para criptografar a senha.

## Siga o princípio do menor privilégio

O princípio do menor privilégio limita usuários e processos ao nível mínimo de acesso necessário para suas tarefas. Siga esse princípio ao escrever código para reduzir o impacto de incidentes de segurança.

Por exemplo, se uma aplicação precisa apenas ler dados de um banco de dados, use uma conta com permissão somente de leitura em vez de uma conta com permissões completas. Isso reduz o risco de um invasor explorar a aplicação para alterar ou excluir dados.

## Mantenha bibliotecas e estruturas de software atualizados

Bibliotecas e estruturas de software podem conter vulnerabilidades exploráveis. Mantenha-os na versão mais recente para reduzir problemas de segurança.

Por exemplo, se a aplicação usar uma biblioteca de terceiros, como `Newtonsoft.Json`, que tenha uma vulnerabilidade, atualize para uma versão que corrija o problema.

## Use um analisador estático de código

Um analisador estático de código identifica possíveis vulnerabilidades antes da execução do código. Use ferramentas como Visual Studio `Code Analysis`, `ReSharper` e `SonarQube` para encontrar e corrigir problemas antes da implantação.

Por exemplo, o Code Analysis do Visual Studio examina código C# e pode identificar injeção de SQL, script entre sites e uso de funções inseguras.

## Use práticas seguras de codificação para aplicações web

Aplicações web estão expostas a riscos como script entre sites, injeção de SQL e injeção de comandos. Use validação de entrada, codificação de saída e consultas parametrizadas para proteger as aplicações.

Ao escrever consultas SQL, use consultas parametrizadas em vez de concatenar entradas de usuários. Elas tratam a entrada como dados, e não como código executável, prevenindo ataques de injeção de SQL.

```csharp
string query = "SELECT * FROM Users WHERE Username = @Username";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    using (SqlCommand command = new SqlCommand(query, connection))
    {
        command.Parameters.AddWithValue("@Username", username);
        connection.Open();
        SqlDataReader reader = command.ExecuteReader();
        // processe os dados
    }
}
```

Valide todas as entradas dos usuários, codifique as saídas e use HTTPS para criptografar os dados transmitidos pela rede.

_____

## Padrões de codificação segura para estruturas C#

estruturas de software C#, como ASP.NET e .NET Core, têm padrões próprios de codificação segura. Siga esses padrões ao desenvolver aplicações com eles.

### ASP.NET

ASP.NET é um estrutura de software web popular para C#. Siga estas práticas:

- Use o sistema de autenticação integrado do ASP.NET em vez de criar um sistema próprio. Por exemplo, use o `Identity` para gerenciar autenticação e autorização.
- Use as funções integradas do ASP.NET para gerar hashes de senhas em vez de criar métodos próprios. A classe `PasswordHasher` gera e verifica hashes com segurança.
- Use o `AntiForgeryToken` integrado do ASP.NET para prevenir falsificação de solicitação entre sites (CSRF). O atributo `ValidateAntiForgeryToken` valida tokens em solicitações POST.
- Use o `OutputCacheAttribute` integrado para impedir o armazenamento em cache de dados sensíveis. Defina políticas de cache para as páginas e evite guardar informações sensíveis.

### .NET Core

.NET Core é um estrutura de software multiplataforma e de código aberto para aplicações modernas baseadas em nuvem. Siga estas práticas:

- Use o sistema de autenticação integrado do .NET Core em vez de criar um sistema próprio. O `Identity` gerencia autenticação e autorização.
- Use funções integradas para gerar hashes de senhas em vez de criar métodos próprios. A classe `PasswordHasher` gera e verifica hashes.
- Use a API de proteção de dados (Data Protection API) integrada do .NET Core para proteger dados sensíveis, como cadeias de conexão e segredos. A classe `DataProtectionProvider` protege os dados com uma chave.
- Use verificações de integridade (Health Checks) para monitorar a integridade da aplicação. O componente intermediário `HealthCheck` pode executar verificações periódicas e alertar sobre problemas.

## Conclusão

Os padrões de codificação segura ajudam a manter o código seguro, confiável e livre de vulnerabilidades. Desenvolvedores C# devem validar entradas, evitar funções inseguras, usar bibliotecas de criptografia e manter as dependências atualizadas. Ao trabalhar com estruturas C#, siga também os padrões de segurança recomendados por eles.

A codificação segura é um processo contínuo que exige acompanhar práticas e ferramentas de segurança. Integrar esses padrões ao processo de desenvolvimento reduz o risco de incidentes de segurança e protege dados sensíveis.

Para começar, familiarize-se com as práticas deste artigo. Identifique áreas de risco no código, como validação de entrada, hash de senhas e gerenciamento de sessões, e aplique as medidas adequadas.

Acompanhe blogs de segurança, participe de conferências e comunidades online para conhecer as tendências e práticas mais recentes.

Promova uma cultura de conscientização sobre segurança na equipe compartilhando boas práticas, organizando treinamentos e aplicando essas medidas no próprio código. Isso ajuda a proteger o código de toda a equipe.

Essas práticas ajudam a manter o código C# seguro e confiável, reduzir incidentes de segurança e proteger dados sensíveis.

## Referências

Estes recursos ajudam a aprender mais sobre codificação segura em C# e sua implementação em projetos:

- [Diretrizes de codificação segura da Microsoft para C# e .NET](https://learn.microsoft.com/en-us/dotnet/standard/security/secure-coding-guidelines)
- [Práticas de codificação segura da OWASP](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [estrutura de software de desenvolvimento seguro de software do NIST](https://csrc.nist.gov/Projects/ssdf)
- [Referência de segurança CIS para Microsoft .NET Framework 4.5](https://www.cisecurity.org/benchmark/microsoft_net_framework_4-5_benchmark/)
- [Security Code Scan - .NET Security Guard](https://security-code-scan.github.io/#NET-Security-Guard)

Esses recursos ajudam os desenvolvedores a aprender práticas de codificação segura e aplicá-las em seus projetos.
