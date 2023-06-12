---
title: "Normas de codificación segura para Python: Buenas prácticas"
date: 2023-02-26
toc: true
draft: false
description: "Aprenda las mejores prácticas de codificación segura en Python para minimizar el riesgo de brechas de seguridad y proteger los datos sensibles."
tags: ["Python", "Codificación segura", "Riesgos de seguridad", "Validación de las entradas", "Bibliotecas criptográficas", "Menor privilegio", "Analizador de código estático", "Aplicaciones web", "Marcos de trabajo de Python", "Django", "Flash", "Sistema de autenticación", "Cifrado de contraseñas", "Sistema de plantillas", "Gestión de sesiones", "MarkupSafe", "WTForms", "Intermitente", "Protección de datos", "Vulnerabilidades", "Codificación segura", "Python", "Riesgos de seguridad", "Validación de entradas", "Bibliotecas criptográficas", "Menor privilegio", "Analizador de código estático", "Aplicaciones web", "Marcos de trabajo de Python", "Django", "Flash", "Sistema de autenticación", "Cifrado de contraseñas", "Sistema de plantillas", "Gestión de sesiones", "MarkupSafe", "WTForms", "Intermitente", "Protección de datos", "Vulnerabilidades", "Seguridad del código Python", "Revisión del código", "Herramientas de análisis estático", "Desarrollo web seguro", "Prácticas de codificación seguras", "Vulnerabilidades de seguridad", "Buenas prácticas de seguridad del código", "Cifrado de datos", "Principio del menor privilegio", "Análisis del código", "Seguridad web"]
cover: "/img/cover/A_cartoon_shield_with_the_word_Python.png"
coverAlt: "Un escudo de dibujos animados con la palabra Python escrita en él para representar las normas de codificación segura"
coverCaption: ""
---
 Prácticas para normas de codificación segura en Python**

### 1. Validación de Entrada

### Validación de Entrada

La entrada de datos por parte del usuario suele ser una fuente importante de riesgos para la seguridad. **La validación de entrada** es el proceso de verificar que la entrada del usuario cumple los criterios esperados y es segura para su uso en la aplicación.

Por ejemplo, cuando un usuario introduce un número de tarjeta de crédito, la entrada sólo debe contener dígitos y ningún carácter especial. Para validar la entrada, los desarrolladores pueden utilizar funciones integradas como `isdigit()` o expresiones regulares para garantizar que la entrada cumple los criterios esperados.

```python
import re

def validate_input(input_string):
    """
    Function to validate input using regular expressions.
    """
    pattern = r"^[0-9]+$"
    if re.match(pattern, input_string):
        return True
    else:
        return False
```

### 2. Evitar el uso de funciones inseguras

Python tiene varias funciones que pueden ser vulnerables a problemas de seguridad si no se usan con cuidado. Funciones como `exec()` `eval()` y `pickle` pueden permitir a los atacantes ejecutar código malicioso. Los desarrolladores deben **evitar el uso de estas funciones** o utilizarlas con precaución restringiendo los parámetros de entrada y utilizándolas solo cuando sea necesario.

Por ejemplo, en lugar de utilizar `eval()` para convertir una cadena en un número entero, los desarrolladores deben utilizar la función `int()` función.
```py
# Instead of using eval function
x = eval('10')

# Use int function
x = int('10')
```

### 3. Utilizar bibliotecas criptográficas

**Librerías de criptografía** tales como [`cryptography`](https://pypi.org/project/cryptography/) and [`pycryptodome`](https://pypi.org/project/pycryptodome/) proporcionan una forma segura de realizar operaciones de cifrado y descifrado. Utiliza estas bibliotecas en lugar de crear métodos de cifrado personalizados, que pueden ser propensos a vulnerabilidades.

Por ejemplo, para cifrar una contraseña, utilice la biblioteca [`cryptography`](https://pypi.org/project/cryptography/) biblioteca como sigue:
```py
from cryptography.fernet import Fernet

def encrypt_password(password):
    """
    Function to encrypt password using cryptography library.
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    return encrypted_password

password = "mypassword"
encrypted_password = encrypt_password(password)
```
En `Fernet` genera una clave, que se utiliza para cifrar la contraseña mediante el objeto `encrypt()` método.

### 4. Siga el Principio de Mínimo Privilegio

**El principio de mínimo privilegio** es una buena práctica de seguridad que restringe a los usuarios o procesos al mínimo nivel de acceso necesario para realizar sus funciones. Los desarrolladores deben seguir este principio al escribir código para minimizar el impacto de las brechas de seguridad.

Por ejemplo, si una aplicación requiere acceso de sólo lectura a una base de datos, debería utilizar una cuenta de base de datos con permisos de sólo lectura en lugar de una cuenta con permisos completos. Esto reduce el riesgo de que un atacante explote la aplicación para modificar o borrar datos.

### 5. Mantenga actualizadas las bibliotecas y los marcos de trabajo

Las librerías y frameworks pueden contener vulnerabilidades de seguridad que pueden ser explotadas por atacantes. Los desarrolladores deben **mantener sus librerías y frameworks actualizados** a la última versión para evitar posibles problemas de seguridad.

Por ejemplo, si la aplicación utiliza una biblioteca de terceros, como [`Requests`](https://pypi.org/project/requests/) que tenga una vulnerabilidad de seguridad, el desarrollador debe actualizar a la última versión de la biblioteca que solucione la vulnerabilidad.

### 6. Utilice un analizador de código estático

**Un analizador de código estático** es una herramienta que puede identificar posibles vulnerabilidades de seguridad en el código antes de que se ejecute. Utilice herramientas como [`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/) para detectar problemas de seguridad en el código y solucionarlos antes de su despliegue.

Por ejemplo, [`bandit`](https://pypi.org/project/bandit/) es un popular analizador de código estático que examina el código Python en busca de posibles vulnerabilidades de seguridad. Puede detectar problemas como contraseñas codificadas, inyección SQL y uso de funciones no seguras.

### 7. Utilice prácticas de codificación seguras para las aplicaciones Web

Las aplicaciones Web son vulnerables a varios riesgos de seguridad como el cross-site scripting, la inyección SQL y la inyección de comandos. Los desarrolladores deben **seguir prácticas de codificación seguras** como la validación de entradas, la codificación de salidas y las consultas parametrizadas para garantizar la seguridad de las aplicaciones web.

Por ejemplo, al escribir consultas SQL, utilice **consultas parametrizadas** en lugar de concatenar la entrada del usuario con la consulta. Las consultas parametrizadas evitan los ataques de inyección SQL al tratar la entrada del usuario como datos y no como código ejecutable.

```py
# Instead of this
query = "SELECT * FROM users WHERE username = '" + username + "';"

# Use parameterized query
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))
```
Los desarrolladores también deben **validar todas las entradas del usuario**, codificar la salida y utilizar HTTPS para cifrar los datos transmitidos a través de la red.

## Estándares de Codificación Segura para Frameworks Python

Frameworks de Python como [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/) tienen sus propias normas de codificación segura. Los desarrolladores deben seguir estos estándares cuando desarrollen aplicaciones utilizando estos frameworks. Estos son algunos estándares de codificación segura para frameworks Python:

### 1. [Django](https://www.djangoproject.com/)

[Django](https://www.djangoproject.com/) is a popular web framework for Python. Here are some secure coding standards for [Django](https://www.djangoproject.com/)

- Utilización [Django](https://www.djangoproject.com/) sistema de **autenticación** integrado en lugar de crear un sistema de autenticación personalizado.
- Utilización [Django](https://www.djangoproject.com/) funciones de hash de contraseña** integradas en lugar de crear métodos de hash de contraseña personalizados.
- Utilice [Django](https://www.djangoproject.com/) **sistema de plantillas** para garantizar que la salida es segura y está libre de vulnerabilidades de secuencias de comandos en sitios cruzados.

Por ejemplo, para utilizar [Django](https://www.djangoproject.com/)'s built-in password hashing function, use the `make_password()` function from the ` módulo.

```python
from [Django](https://www.djangoproject.com/).contrib.auth.hashers import make_password

password = "mypassword"
hashed_password = make_password(password)
```

### 2. [Flask](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/) is a micro web framework for Python. Here are some secure coding standards for [Flask](https://flask.palletsprojects.com/)

- Utilización [Flask](https://flask.palletsprojects.com/) Sistema de gestión de sesiones** integrado para garantizar la gestión segura de las sesiones.
- Utilización [Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) para garantizar que la salida sea segura y esté libre de vulnerabilidades de secuencias de comandos en sitios cruzados.
- Utilización [Flask](https://flask.palletsprojects.com/)'s [`WTForms`](https://pypi.org/project/WTForms/) para gestionar la validación de la entrada del usuario y garantizar que la entrada está libre de riesgos de seguridad.
- Utilización [Flask](https://flask.palletsprojects.com/)'s [`Blinker`](https://pypi.org/project/blinker/) para el manejo seguro de señales.

Por ejemplo, para utilizar [Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) importarla y utilizarla para escapar etiquetas HTML de la salida.
```py
from markupsafe import escape

@app.route('/')
def hello():
    name = "<script>alert('xss');</script>"
    return 'Hello, ' + escape(name)
```
______

## Utilizar tus conocimientos y ¿qué hacer ahora?

1. **Empieza a implementar estas mejores prácticas en tu código Python hoy mismo** para minimizar el riesgo de brechas de seguridad y proteger datos sensibles. Puedes empezar identificando áreas en tu código que son susceptibles a riesgos de seguridad, como validación de entrada, hash de contraseñas y gestión de sesiones. A continuación, puede implementar las mejores prácticas como las que se discuten en este artículo para asegurar su código. Por ejemplo, puede utilizar las expresiones regulares incorporadas en Python para validar la entrada del usuario o utilizar una biblioteca segura de hash de contraseñas como [`bcrypt`](https://pypi.org/project/bcrypt/)

2. **Revise su código base existente en busca de posibles vulnerabilidades de seguridad** y utilice analizadores de código estático como [`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/) para detectar y solucionar cualquier problema. También puede utilizar la revisión manual del código para identificar problemas de seguridad que los analizadores estáticos de código no detectan. Busque vulnerabilidades comunes como inyección SQL, cross-site scripting y problemas de validación de entradas. Una vez identificadas las posibles vulnerabilidades de seguridad, puede utilizar las mejores prácticas para solucionar los problemas.

3. **Manténgase al día con las últimas mejores prácticas y herramientas de seguridad** para asegurarse de que su código sigue siendo seguro y libre de vulnerabilidades. Sigue blogs de seguridad, asiste a conferencias y participa en comunidades online para estar al día de las últimas tendencias y prácticas de seguridad. Mantenga actualizadas sus bibliotecas y frameworks para asegurarse de que utiliza las últimas versiones seguras.

4. **Únete a comunidades online y asiste a eventos** donde puedas aprender de expertos y otros desarrolladores sobre prácticas de codificación segura para Python. Busca comunidades y foros en línea en los que puedas debatir cuestiones de seguridad con otros desarrolladores, aprender sobre nuevas tendencias de seguridad y compartir tus propios conocimientos. Asiste a eventos como conferencias, seminarios web y reuniones para aprender de expertos en seguridad y otros desarrolladores.

5. **Comparte estas buenas prácticas con tu equipo o colegas** para promover una cultura de concienciación sobre la seguridad y animar a otros a adoptar prácticas de codificación seguras en sus proyectos Python. Organiza sesiones de formación sobre seguridad, comparte artículos y recursos sobre prácticas de codificación seguras y predica con el ejemplo implementando estas mejores prácticas en tu propio código. Al promover una cultura de concienciación sobre la seguridad, puedes ayudar a garantizar que el código de tu equipo sea seguro y esté libre de vulnerabilidades.


## Conclusión

Los estándares de codificación segura son esenciales para asegurar que el código es seguro, fiable y libre de vulnerabilidades. Python es un lenguaje de programación popular que requiere que los desarrolladores sigan estándares de codificación segura para prevenir riesgos de seguridad. Siguiendo las mejores prácticas como la validación de entradas, evitando funciones inseguras, usando librerías criptográficas, y manteniendo las librerías y frameworks actualizados, los desarrolladores pueden asegurar que su código es seguro y libre de vulnerabilidades. Cuando se utilizan frameworks de Python, los desarrolladores deben seguir las normas de codificación segura recomendadas por el framework.

Adoptar estándares de codificación segura es un proceso continuo que requiere que los desarrolladores se mantengan actualizados con las últimas mejores prácticas y herramientas de seguridad. Al incorporar estándares de codificación segura en el proceso de desarrollo, los desarrolladores pueden minimizar el riesgo de brechas de seguridad y proteger los datos sensibles.

