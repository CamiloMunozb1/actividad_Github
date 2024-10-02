from api.uso import uso_aplicacion
from api.llamada import llamada_api

while True:
    print(
        """
        BIENVENIDO A LA APLICACION DE LA ACTIVIDAD DE USUARIOS EN GITHUB
        1. Ingresar nombre de usuarios.
        2. Como usar la aplicacion.
        3. Salir.
        """
    )
    try:
        usuario = int(input("ingrese una opcion: "))
        if usuario == 1:
            llamada_api()
        elif usuario == 2:
            uso_aplicacion()
        elif usuario == 3:
            print("Muchas gracias por usar usar la actividad del usuario de GitHub ")
            break
    except ValueError:
        print("Error en la digitacion, volver a digitar.")