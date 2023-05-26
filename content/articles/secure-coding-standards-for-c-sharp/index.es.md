---
title: "Normas de codificación segura para desarrolladores de C#"
date: 2023-02-28
toc: true
draft: false
description: "Aprenda las mejores prácticas de codificación segura en C# para minimizar el riesgo de infracciones de seguridad y proteger los datos confidenciales."
tags: ["Codificación segura", "C desarrollo afilado", "Programación en C Sharp", "prácticas de codificación seguras", "Seguridad C Sharp", "Seguridad ASP.NET", "Seguridad en .NET Core", "validación de entrada", "hash de contraseña", "criptografía", "menor privilegio", "analizador de código estático", "seguridad de las aplicaciones web", "Prevención de inyecciones SQL", "prevención de secuencias de comandos en sitios cruzados", "protección de datos", "controles sanitarios", "gestión de sesiones", "Buenas prácticas de OWASP", "Normas de codificación segura de C Sharp", "C Directrices de seguridad de Sharp", "consejos para una codificación segura", "desarrollo seguro de software", "marcos de codificación segura", "técnicas de codificación segura", "recomendaciones para una codificación segura", "Programación segura en C Sharp", "vulnerabilidades de la codificación segura", "herramientas de codificación segura", "tutoriales de codificación segura", "Buenas prácticas de codificación segura en C Sharp", "Directrices de codificación segura de C Sharp", "Normas de codificación segura para desarrolladores de C Sharp", "C Prácticas de codificación segura", "Cómo aplicar la codificación segura en C Sharp", "Consejos de codificación segura para programadores de C Sharp", "Codificación segura en aplicaciones web C Sharp", "Marcos de codificación segura C Sharp", "Técnicas de codificación segura para desarrolladores de C Sharp", "Herramientas de codificación segura C Sharp"]
cover: "/img/cover/A_cartoon_developer_with_a_lock_icon_as_the_head_surrounded.png"
coverAlt: " Un desarrollador de dibujos animados con el icono de una cerradura como cabeza, rodeado de código y protegido por un cortafuegos."
coverCaption: ""
---

La codificación segura es esencial para garantizar que el código sea seguro, fiable y libre de vulnerabilidades. C Sharp es un lenguaje de programación popular que requiere que los desarrolladores sigan estándares de codificación segura para prevenir riesgos de seguridad. Siguiendo las mejores prácticas, como la validación de entradas, evitando funciones no seguras, utilizando bibliotecas de criptografía y manteniendo actualizadas las bibliotecas y los marcos de trabajo, los desarrolladores pueden garantizar que su código sea seguro y esté libre de vulnerabilidades.

_____

## Validación de entradas

La entrada de datos por parte del usuario suele ser una fuente importante de riesgos para la seguridad. La validación de la entrada es el proceso de verificar que la entrada del usuario cumple los criterios esperados y es segura para su uso en la aplicación. Por ejemplo, cuando un usuario introduce un número de tarjeta de crédito, la entrada sólo debe contener dígitos y ningún carácter especial. Para validar la entrada, los desarrolladores pueden utilizar clases integradas como `Regex` para garantizar que la entrada cumple los criterios esperados.

```csharp
public static bool ValidateInput(string inputString)
{
    bool isValid = false;
    // Check if input string contains only digits
    if (Regex.IsMatch(inputString, @"^\d+$"))
    {
        isValid = true;
    }
    return isValid;
}
```

Este método utiliza expresiones regulares para comprobar si la cadena de entrada sólo contiene dígitos. Devuelve un valor booleano que indica si la entrada es válida o no.

## Evite usar funciones inseguras
C Sharp tiene varias funciones que pueden ser vulnerables a problemas de seguridad si no se usan con cuidado. Funciones como `Process.Start()` `Reflection` y `Deserialization` pueden permitir a los atacantes ejecutar código malicioso. Los desarrolladores deben evitar el uso de estas funciones o utilizarlas con precaución restringiendo los parámetros de entrada y utilizándolas solo cuando sea necesario.

Por ejemplo, en lugar de utilizar `Process.Start()` para iniciar un proceso externo, los desarrolladores deben utilizar la función `Process.StartInfo` para proporcionar argumentos y restricciones de seguridad.
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
## Utilizar bibliotecas de criptografía
Las bibliotecas de criptografía como Bouncy Castle y las API de criptografía de .NET Framework proporcionan una forma segura de realizar operaciones de cifrado y descifrado. Utilice estas bibliotecas en lugar de crear métodos de cifrado personalizados, que pueden ser propensos a vulnerabilidades.

Por ejemplo, para cifrar una contraseña, utilice la biblioteca `Rfc2898DeriveBytes` de las API de criptografía de .NET Framework de la siguiente manera:
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
En `Rfc2898DeriveBytes` genera una sal y la utiliza para derivar una clave a partir de la contraseña. La clave resultante se utiliza para cifrar la contraseña.

## Sigue el Principio de Mínimo Privilegio

El principio de mínimo privilegio es una buena práctica de seguridad que restringe a los usuarios o procesos al mínimo nivel de acceso necesario para realizar sus funciones. Los desarrolladores deben seguir este principio al escribir código para minimizar el impacto de las brechas de seguridad.

Por ejemplo, si una aplicación requiere acceso de sólo lectura a una base de datos, debería utilizar una cuenta de base de datos con permisos de sólo lectura en lugar de una cuenta con permisos completos. Esto reduce el riesgo de que un atacante explote la aplicación para modificar o borrar datos.

## Mantener actualizadas las bibliotecas y los marcos de trabajo

Las librerías y frameworks pueden contener vulnerabilidades de seguridad que pueden ser explotadas por atacantes. Los desarrolladores deben mantener sus bibliotecas y frameworks actualizados a la última versión para evitar posibles problemas de seguridad.

Por ejemplo, si la aplicación utiliza una biblioteca de terceros, como `Newtonsoft.Json` que tenga una vulnerabilidad de seguridad, el desarrollador debe actualizar a la última versión de la biblioteca que solucione la vulnerabilidad.

## Utilizar un analizador de código estático

Un analizador de código estático es una herramienta que puede identificar posibles vulnerabilidades de seguridad en el código antes de que se ejecute. Utilice herramientas como Code `Analysis` `ReSharper` y `SonarQube` para detectar problemas de seguridad en el código y solucionarlos antes de su despliegue.

Por ejemplo, el análisis de código de Visual Studio es un conocido analizador de código estático que examina el código C Sharp en busca de posibles vulnerabilidades de seguridad. Puede detectar problemas como inyecciones SQL, secuencias de comandos entre sitios y el uso de funciones no seguras.

## Utilice prácticas de codificación seguras para las aplicaciones web

Las aplicaciones Web son vulnerables a varios riesgos de seguridad como el cross-site scripting, la inyección SQL y la inyección de comandos. Los desarrolladores deben seguir prácticas de codificación seguras como la validación de entrada, la codificación de salida y las consultas parametrizadas para garantizar que las aplicaciones web sean seguras.

Por ejemplo, al escribir consultas SQL, utilice consultas parametrizadas en lugar de concatenar la entrada del usuario con la consulta. Las consultas parametrizadas evitan los ataques de inyección SQL al tratar la entrada del usuario como datos y no como código ejecutable.

```csharp
string query = "SELECT * FROM Users WHERE Username = @Username";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    using (SqlCommand command = new SqlCommand(query, connection))
    {
        command.Parameters.AddWithValue("@Username", username);
        connection.Open();
        SqlDataReader reader = command.ExecuteReader();
        // process the data
    }
}
```

Los desarrolladores también deben validar todas las entradas de los usuarios, codificar las salidas y utilizar HTTPS para cifrar los datos transmitidos por la red.

_____

## Estándares de Codificación Segura para Frameworks C Sharp

Los frameworks C Sharp como ASP.NET y .NET Core tienen sus propios estándares de codificación segura. Los desarrolladores deben seguir estos estándares cuando desarrollen aplicaciones utilizando estos frameworks.

### ASP.NET
ASP.NET es un popular framework web para C Sharp. Aquí hay algunos estándares de codificación segura para ASP.NET:

- Utilice el sistema de autenticación integrado de ASP.NET en lugar de crear un sistema de autenticación personalizado. Por ejemplo, puede utilizar el sistema de autenticación de ASP.NET `Identity` para gestionar la autenticación y autorización de usuarios.
- Utilice las funciones de hash de contraseñas integradas de ASP.NET en lugar de crear métodos de hash de contraseñas personalizados. Por ejemplo, puede utilizar las funciones `PasswordHasher` para extraer y verificar contraseñas de forma segura.
- Utilice la clase `AntiForgeryToken` para evitar ataques de falsificación de petición en sitios cruzados (CSRF). Por ejemplo, puede utilizar la función `ValidateAntiForgeryToken` para validar tokens anti-falsificación en peticiones POST.
- Utilice el atributo `OutputCacheAttribute` para evitar el almacenamiento en caché de datos sensibles. Por ejemplo, puede utilizar la opción `OutputCacheAttribute` para establecer políticas de caché para sus páginas web y evitar que se almacenen en caché datos confidenciales.

### .NET Core
.NET Core es un marco multiplataforma de código abierto para crear aplicaciones modernas basadas en la nube. Estas son algunas normas de codificación segura para .NET Core:

- Utilice el sistema de autenticación integrado de .NET Core en lugar de crear un sistema de autenticación personalizado. Por ejemplo, puede utilizar el sistema de autenticación integrado de .NET Core `Identity` para gestionar la autenticación y autorización de usuarios.
- Utilice las funciones hash de contraseña integradas de .NET Core en lugar de crear métodos hash de contraseña personalizados. Por ejemplo, puede utilizar las funciones `PasswordHasher` para extraer y verificar contraseñas de forma segura.
- Utilice la API de protección de datos integrada de .NET Core para proteger datos confidenciales como cadenas de conexión y secretos. Por ejemplo, puede utilizar la clase `DataProtectionProvider` para proteger los datos confidenciales con una clave.
- Utilice las comprobaciones de estado integradas en .NET Core para supervisar el estado de su aplicación. Por ejemplo, puede utilizar la clase `HealthCheck` para realizar comprobaciones periódicas de la salud de su aplicación y alertarle de cualquier problema.


## Conclusión
Los estándares de codificación segura son esenciales para asegurar que el código es seguro, fiable y libre de vulnerabilidades. C Sharp es un lenguaje de programación popular que requiere que los desarrolladores sigan estándares de codificación segura para prevenir riesgos de seguridad. Siguiendo las mejores prácticas como la validación de entrada, evitando funciones inseguras, usando librerías criptográficas, y manteniendo las librerías y frameworks actualizados, los desarrolladores pueden asegurar que su código es seguro y libre de vulnerabilidades. Al utilizar marcos de trabajo en C Sharp, los desarrolladores deben seguir las normas de codificación segura recomendadas por el marco de trabajo.

Adoptar estándares de codificación segura es un proceso continuo que requiere que los desarrolladores se mantengan actualizados con las últimas mejores prácticas y herramientas de seguridad. Al incorporar estándares de codificación segura en el proceso de desarrollo, los desarrolladores pueden minimizar el riesgo de brechas de seguridad y proteger los datos sensibles.

Para empezar con la codificación segura en C Sharp, los desarrolladores pueden empezar por familiarizarse con las mejores prácticas discutidas en este artículo. Deben identificar las áreas en su código que son susceptibles a los riesgos de seguridad, tales como la validación de entrada, hash de contraseña, y la gestión de sesiones. Luego pueden implementar las mejores prácticas como las discutidas en este artículo para asegurar su código.

Los desarrolladores también deben mantenerse al día de las últimas tendencias y prácticas de seguridad siguiendo blogs de seguridad, asistiendo a conferencias y participando en comunidades en línea. Al mantenerse actualizados, pueden mantener su código seguro y libre de vulnerabilidades.

Por último, los desarrolladores deben promover una cultura de concienciación sobre la seguridad compartiendo las mejores prácticas con su equipo o colegas. Deben organizar sesiones de formación sobre seguridad, compartir artículos y recursos sobre prácticas de codificación seguras y dar ejemplo aplicando estas buenas prácticas en su propio código. Al promover una cultura de concienciación sobre la seguridad, pueden ayudar a garantizar que el código de su equipo sea seguro y esté libre de vulnerabilidades.

Siguiendo estas buenas prácticas, los desarrolladores pueden asegurarse de que su código C Sharp es seguro y fiable, y pueden ayudar a prevenir brechas de seguridad y proteger datos sensibles.

## Referencias

Aquí hay algunos recursos útiles para aprender más sobre las prácticas de codificación segura en C Sharp:

- [Microsoft's Secure Coding Guidelines for C Sharp and .NET](https://learn.microsoft.com/en-us/dotnet/standard/security/secure-coding-guidelines)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [NIST's Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)
- [CIS Microsoft .NET Framework 4.5 Benchmark](https://www.cisecurity.org/benchmark/microsoft_net_framework_4-5_benchmark/)
- [Security Code Scan - .NET Security Guard](https://security-code-scan.github.io/#NET-Security-Guard)

Siguiendo estos recursos, los desarrolladores pueden aprender más sobre prácticas de codificación segura en C Sharp y cómo implementarlas en sus proyectos.
