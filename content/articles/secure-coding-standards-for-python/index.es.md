---
title: "Secure Coding Standards for Python: Best Practices"
date: 2023-02-26
toc: true
draft: false
description: "Learn the best practices for secure coding in Python to minimize the risk of security breaches and protect sensitive data."
tags: ["Python", "Secure coding", "Security risks", "Input validation", "Cryptography libraries", "Least privilege", "Static code analyzer", "Web applications", "Python frameworks", "Django", "Flask", "Authentication system", "Password hashing", "Template system", "Session management", "MarkupSafe", "WTForms", "Blinker", "Data protection", "Vulnerabilities"]
cover: "/img/cover/A_cartoon_shield_with_the_word_Python.png"
coverAlt: "A cartoon shield with the word Python written on it to represent secure coding standards"
coverCaption: ""
---
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
```py
# Instead of using eval function
x = eval('10')

# Use int function
x = int('10')
```
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
```py
# Instead of this
query = "SELECT * FROM users WHERE username = '" + username + "';"

# Use parameterized query
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))
```
```python
from [Django](https://www.djangoproject.com/).contrib.auth.hashers import make_password

password = "mypassword"
hashed_password = make_password(password)
```
```py
from markupsafe import escape

@app.route('/')
def hello():
    name = "<script>alert('xss');</script>"
    return 'Hello, ' + escape(name)
```

**Mejores prácticas para estándares de codificación segura en Python**  ### 1. Validacion de entrada  ### Validacion de entrada  La entrada del usuario suele ser una fuente importante de riesgos de seguridad. **Validación de entrada** es el proceso de verificar que la entrada del usuario cumple con los criterios esperados y es seguro para usar en la aplicación.  Por ejemplo, cuando un usuario ingresa un número de tarjeta de crédito, la entrada solo debe contener dígitos y ningún carácter especial. Para validar la entrada, los desarrolladores pueden usar funciones integradas como `isdigit()` o expresiones regulares para garantizar que la entrada cumpla con los criterios esperados.   ### 2. Evite el uso de funciones no seguras  Python tiene varias funciones que pueden ser vulnerables a problemas de seguridad si no se usan con cuidado. Funciones como `exec()`, `eval()` y `pickle` pueden permitir a los atacantes ejecutar código malicioso. Los desarrolladores deben **evitar usar estas funciones** o usarlas con precaución restringiendo los parámetros de entrada y usándolos solo cuando sea necesario.  Por ejemplo, en lugar de usar la función `eval()` para convertir una cadena en un número entero, los desarrolladores no podrán usar la función `int()`.  ### 3. Usar bibliotecas criptográficas  **Bibliotecas de criptografía** como [`cryptography`](https://pypi.org/project/cryptography/) y [`pycryptodome`](https://pypi.org/project/pycryptodome/) asegurando una forma de realizar operaciones de cifrado y descifrado. Use estas bibliotecas en lugar de crear métodos de grabación personalizados, que pueden ser probables vulnerabilidades.  Por ejemplo, para cifrar una contraseña, use la biblioteca [`cryptography`](https://pypi.org/project/cryptography/) de la siguiente manera: El objeto `Fernet` genera una clave, que se utiliza para cifrar la contraseña mediante el método `encrypt()`.  ### 4. Sigue el Principio del Mínimo Privilegio  **El principio de privilegio mínimo** es una práctica recomendada de seguridad que restringe a los usuarios o procesos al nivel mínimo de acceso necesario para realizar sus funciones. Los desarrolladores deben seguir este principio al escribir código para minimizar el impacto de las infracciones de seguridad.  Por ejemplo, si una aplicación requiere acceso de lectura en solitario a una base de datos, debe usar una cuenta de base de datos con permisos de lectura en solitario en lugar de una cuenta con permisos completos. Esto reduce el riesgo de que un atacante explote la aplicación para modificar o eliminar datos.  ### 5. Mantenga las bibliotecas y los marcos actualizados  Las bibliotecas y los marcos pueden contener vulnerabilidades de seguridad que los atacantes pueden explotar. Los desarrolladores deben **mantener sus bibliotecas y marcos actualizados** a la última versión para evitar posibles problemas de seguridad.  Por ejemplo, si la aplicación usa una biblioteca de terceros, como [`Requests`](https://pypi.org/project/requests/), que tiene una vulnerabilidad de seguridad, el desarrollador debe actualizar a la última versión de la biblioteca que aborda la vulnerabilidad.  ### 6. Use un analizador de código estático  **Un posible analizador de código estático** es una herramienta que puede identificar vulnerabilidades de seguridad en el código antes de ejecutarlo. Utilice herramientas como [`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/) y [`Pyflakes`] (https ://pypi.org/project/pyflakes/) para detectar problemas de seguridad en el código y solucionarlos antes de la implementación.  Por ejemplo, [`bandit`](https://pypi.org/project/bandit/) es un analizador de código estático popular que examina el código de Python en busca de posibles vulnerabilidades de seguridad. Puede detectar problemas como contraseñas codificadas, inyección SQL y uso de funciones no seguras.  ### 7. Utilice codificación segura para aplicaciones web  Las aplicaciones web son vulnerables a varios riesgos de seguridad, como secuencias de comandos entre sitios, inyección SQL e inyección de comandos. Los desarrolladores deben **seguir prácticas de codificación segura**, como validación de entrada, codificación de salida y consultas parametrizadas para garantizar que las aplicaciones web sean seguras.  Por ejemplo, al escribir consultas SQL, use **consultas parametrizadas** en lugar de concatenar la entrada del usuario con la consulta. Las consultas parametrizadas evitan los ataques de inyección SQL al tratar la entrada del usuario como datos en lugar de código ejecutable.  Los desarrolladores también deben **validar todas las entradas del usuario**, codificar la salida y usar HTTPS para cifrar los datos transmitidos a través de la red.  ## Estándares de codificación segura para Python Frameworks  Los marcos de Python como [Django](https://www.djangoproject.com/) y [Flask](https://flask.palletsprojects.com/) tienen sus estándares de codificación seguros. Los desarrolladores deben seguir estos estándares al desarrollar aplicaciones utilizando estos marcos. Aquí hay algunos estándares de codificación de seguros para los marcos de trabajo de Python:  ### 1. [Django](https://www.djangoproject.com/)  [Django](https://www.djangoproject.com/) es un marco web popular para Python. Aquí hay algunos estándares de codificación de seguros para [Django] (https://www.djangoproject.com/):  - Utilice el **sistema de autenticación** integrado de [Django](https://www.djangoproject.com/) en lugar de crear un sistema de autenticación personalizado. - Use las **funciones de hash de contraseñas** integradas de [Django](https://www.djangoproject.com/) en lugar de crear métodos personalizados de hash de contraseñas. - Utilice el **sistema de plantillas** de [Django](https://www.djangoproject.com/) para asegurarse de que la salida sea segura y esté libre de vulnerabilidades de secuencias de comandos entre sitios.  Por ejemplo, para usar la función incorporada de hash de contraseñas de [Django](https://www.djangoproject.com/), use la función `make_password()` del módulo `django.contrib.auth.hashers`.   ### 2. [Frasco](https://flask.palletsprojects.com/) [Flask](https://flask.palletsprojects.com/) es un micro marco web para Python. Estos son algunos estándares de codificación segura para [Flask](https://flask.palletsprojects.com/):  - Utilice el **sistema de gestión de sesiones** integrado de [Flask](https://flask.palletsprojects.com/) para garantizar un manejo seguro de las sesiones. - Use la biblioteca [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) de [Flask](https://flask.palletsprojects.com/) para asegurarse de que la salida sea segura y libre de cruces. -vulnerabilidades de secuencias de comandos del sitio. - Use la biblioteca [`WTForms`](https://pypi.org/project/WTForms/) de [Flask](https://flask.palletsprojects.com/) para manejar la validación de entrada del usuario y garantizar de que la entrada sea gratuita de los riesgos de seguridad. - Use la biblioteca [`Blinker`](https://pypi.org/project/blinker/) de [Flask](https://flask.palletsprojects.com/) para el manejo seguro de señales.  Por ejemplo, para usar la biblioteca [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) de [Flask](https://flask.palletsprojects.com/), impórtelo y utilícelo para escapar Etiquetas HTML de la salida. ______  ## ¿Usando su conocimiento y qué hacer ahora?  1. **Comience a implementar estas prácticas recomendadass en su código Python hoy mismo** para minimizar el riesgo de infracciones de seguridad y proteger los datos confidenciales. Puede comenzar identificando áreas en su código que son susceptibles a riesgos de seguridad, como la validación de entrada, el hash de contraseña y la administración de sesiones. A continuación, puede implementar prácticas recomendadas como las que se analizan en este artículo para proteger su código. Por ejemplo, puede usar las expresiones regulares integradas de Python para validar la entrada del usuario o usar una biblioteca segura de hash de contraseñas como [`bcrypt`](https://pypi.org/project/bcrypt/).  2. **Revise su base de código existente en busca de posibles vulnerabilidades de seguridad** y use analizadores de código estático como [`bandit`](https://pypi.org/project/bandit/), [`Pylint` ](https://pypi.org/project/pylint/) y [`Pyflakes`](https://pypi.org/project/pyflakes/) para detectar y solucionar cualquier problema. También puede usar la revisión manual de código para identificar problemas de seguridad que los analizadores de código estático no pueden detectar. Busque vulnerabilidades comunes como inyección SQL, secuencias de comandos entre sitios y problemas de validación de entrada. Una vez que identifique las posibles vulnerabilidades de seguridad, puede utilizar las mejores prácticas para solucionar los problemas.  3. **Manténgase actualizado con las mejores prácticas y herramientas de seguridad más recientes** para garantizar que su código permanezca seguro y libre de vulnerabilidades. Siga blogs de seguridad, asista a conferencias y participe en comunidades en línea para mantenerse actualizado con las últimas tendencias y prácticas de seguridad. Mantenga sus bibliotecas y marcos actualizados para asegurarse de que está utilizando las últimas versiones seguras.  4. **Únase a comunidades en línea y asista a eventos** donde puede aprender de expertos y otros desarrolladores sobre prácticas de codificación segura para Python. Busque comunidades y foros en línea donde pueda discutir problemas de seguridad con otros desarrolladores, conocer nuevas tendencias de seguridad y compartir su propio conocimiento. Asista a eventos como conferencias, seminarios web y reuniones para aprender de los expertos en seguridad y otros desarrolladores.  5. **Comparta estas mejores prácticas con su equipo o colegas** para promover una cultura de concienciación sobre la seguridad y fomentar a otros a adoptar prácticas de codificación seguras en sus proyectos de Python. Organice sesiones de capacitación en seguridad, comparta artículos y recursos sobre prácticas de codificación segura y dé el ejemplo implementando estas mejores prácticas en su propio código. Al promover una cultura de concienciación sobre la seguridad, puede ayudar a garantizar que el código de su equipo sea seguro y esté libre de vulnerabilidades.   ## Conclusión  Los estándares de codificación segura son esenciales para garantizar que el código sea seguro, confiable y libre de vulnerabilidades. Python es un lenguaje de programación popular que requiere que los desarrolladores sigan estándares de codificación seguros para evitar riesgos de seguridad. Al seguir las mejores prácticas, como la validación de entrada, evitar funciones no seguras, usar bibliotecas de criptografía y mantener las bibliotecas y los marcos actualizados, los desarrolladores pueden detectar que su código sea seguro y esté libre de vulnerabilidades. Al usar los marcos de Python, los desarrolladores deben seguir los estándares de codificación seguros recomendados por el marco.  La adopción de estándares de codificación segura es un proceso continuo que requiere que los desarrolladores se mantengan actualizados con las mejores prácticas y herramientas de seguridad más recientes. Al incorporar estándares de codificación de seguros en el proceso de desarrollo, los desarrolladores pueden minimizar el riesgo de infracciones de seguridad y proteger los datos confidenciales. 