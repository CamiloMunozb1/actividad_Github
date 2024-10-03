
# IMPORTACIONES DE FUNCIONES PARA EL INDEX
from api.uso import uso_aplicacion
from api.llamada import llamada_api


while True:

    # MENU DEL USUARIO PARA SELECCIONAR EL USO DE LA API O COMO SE USA LA APLICACION

    print(
        """
        BIENVENIDO A LA APLICACION DE LA ACTIVIDAD DE USUARIOS EN GITHUB
        1. Ingresar nombre de usuarios.
        2. Como usar la aplicacion.
        3. Salir.
        """
    )
    try:

        # VARIABLE PARA INGRESO DE UNA OPCION PARA EL USUARIO

        usuario = int(input("ingrese una opcion: "))

        # LLAMADAS A LAS FUNCIONES SEGUN LA OPCION DEL USUARIO

        if usuario == 1:
            llamada_api()
        elif usuario == 2:
            uso_aplicacion()
        elif usuario == 3:

            # MENSAJE DE DESPEDIDA Y SALIDA DEL USUARIO

            print("Muchas gracias por usar usar la actividad del usuario de GitHub ")
            break
    
    # MANEJO DE ERRORES
    
    except ValueError:
        print("Error en la digitacion, volver a digitar.")