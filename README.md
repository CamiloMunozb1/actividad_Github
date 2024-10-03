## Actividad GitHub
Este proyecto tiene como objetivo demostrar el uso de la API de GitHub para acceder y gestionar información relacionada con los repositorios de un usuario. A través de este proyecto, podrás interactuar con tus repositorios de GitHub de manera programática utilizando la autenticación mediante un token personal.

## Requisitos previos
Antes de comenzar, asegúrate de tener lo siguiente:
-Python 3.x instalado en tu máquina.
-Una cuenta de GitHub activa.
-Un token de autenticación personal de GitHub (instrucciones abajo).

## Instalación
1. Clona este repositorio en tu máquina local:
   git clone https://github.com/CamiloMunozb1/actividad_Github.git
2. Instala las dependencias necesarias con pip:
   pip install -r requirements.txt
   
## Cómo obtener un token de autenticación personal en GitHub
Para interactuar con la API de GitHub, necesitarás un token de autenticación personal. Sigue estos pasos para generarlo:

1. Inicia sesión en tu cuenta de GitHub.
2. En la esquina superior derecha de cualquier página, haz clic en tu foto de perfil y selecciona Configuración.
3. En el menú de la izquierda, selecciona Desarrolladores o Developer settings.
4. En la sección Tokens de acceso personal o Personal access tokens, selecciona Tokens clásicos (Classic) o, si prefieres, Tokens finos (Fine-grained) para tener un control más detallado de los permisos.
5. Haz clic en Generar nuevo token (Generate new token).
6. Asigna un nombre descriptivo al token y selecciona las casillas de permisos que necesites. Para este proyecto, asegúrate de habilitar los permisos de repos (repositorios).
7. Haz clic en Generar token.
8. Copia el token que aparece. Este token se mostrará solo una vez, así que asegúrate de almacenarlo en un lugar seguro.

## Uso
Una vez tengas el token, pegalo en "Authorization": f"{token_autentificacion}" en las llaves y ejecuta el programa.

## Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request con tus cambios.

## Licencia
Este proyecto está bajo la licencia MIT.
