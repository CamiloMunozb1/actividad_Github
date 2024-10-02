import requests

def llamada_api():
    try:
        nombre_usuario = str(input("Ingresa el numero de usuario: "))

        # URL y token

        url = f"https://api.github.com/users/{nombre_usuario}/events"
        headers = {
            "Authorization": f"{token_autentificacion}",
            "Accept": "application/vnd.github.v3+json"
        }


        # Realizar la petición GET con los headers

        respuesta = requests.get(url, headers=headers)
        peticion = respuesta.json()

        limite = 2

        # Mostrar información específica de los eventos

        for event in peticion[:limite]:
            event_type = event['type']
            repo_name = event['repo']['name']
            created_at = event['created_at']
            actor = event['actor']['login']
            
            print(f"Tipo de evento: {event_type}")
            print(f"Repositorio: {repo_name}")
            print(f"Fecha: {created_at}")
            print(f"Actor: {actor}")
            print("-" * 40)

    except ValueError:
        print("Error de validacion, volver a ingresar nombre.")