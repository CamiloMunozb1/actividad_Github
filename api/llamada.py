# USO DE LA LIBRERIA "requests" PARA MANEJAR LA API

import requests

# USO DE UNA FUNCION QUE SE USARA EN EL INDEX

def llamada_api():
    try:

        # ENTRADA DE USUARIO PARA INGRESAR EL NOMBRE DE USUARIO DE GITHUB

        nombre_usuario = str(input("Ingresa el numero de usuario: "))

        # SE DEFINE LA URL/EVENTS PARA VER LOS EVENTOS RECIENTES DEL USUARIO A CONSULTAR

        url = f"https://api.github.com/users/{nombre_usuario}/events"


        headers = {

            # EN LA AUTENTIFICACION SE USA EL TOKEN GENERADO POR GITHUB PARA CADA USUARIO

            "Authorization": f"{token_autentificacion}",

            # EN LA ACEPTACION SE USA LA VERSION DE LA API DE GITHUB Y EL FORMATO EN EL QUE SE ENTREGAN LOS DATOS

            "Accept": "application/vnd.github.v3+json"
        }


        # SE REALIZAN LAS PETICIONES A LA API CON LA URL Y LOS HEADERS ANTES PROPUESTOS

        respuesta = requests.get(url, headers=headers)
        peticion = respuesta.json()

        # SE PONE EL LIMITE DE LOS DOS EVENTOS MAS RECIENTES DEL REPOSITORIO DE CODIGO

        limite = 2

        # SE ITERA ENTRE LOS EVENTOS Y LA PETICION CON EL LIMITE DE LOS DOS EVENTOS

        for event in peticion[:limite]:

            # SE REALIZA EL ANALISIS DE LOS EVENTOS, COMO EL TIPO DE EVENTO

            event_type = event['type']

            # SE ANALIZA EL REPOSITORIO Y EL NOMBRE DE ESTE

            repo_name = event['repo']['name']

            # SE ANALIZA LA FECHA DE CREACION DEL REPOSITORIO

            created_at = event['created_at']

            # SE ANALIZA EL CREADOR DEL REPOSITORIO

            actor = event['actor']['login']
            
            # SE IMPRIMEN LOS RESULTAODS

            print(f"Tipo de evento: {event_type}")
            print(f"Repositorio: {repo_name}")
            print(f"Fecha: {created_at}")
            print(f"Actor: {actor}")

            # SE USAM LOS GUIONES MEDIOS PARA SAPARAR CADA EVENTO

            print("-" * 40)

    # MANEJO DE ERRORES
    
    except ValueError:
        print("Error de validacion, volver a ingresar nombre.")