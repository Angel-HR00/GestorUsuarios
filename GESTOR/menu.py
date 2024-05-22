import os
import helpers
import database as db

def Iniciar():
    while True:
        helpers.clean_screen() #clean screen
        
        print("===========================")
        print("Bienvenido al gestor")
        print("===========================")
        print("[1] Para listar clientes")
        print("[2] Para buscar cliente")
        print("[3] Para añadir cliente ")
        print("[4] Para modificar cliente ")
        print("[5] Para borrar cliente ")
        print("[6] Para cerrar gestor ")
        print("===========================")
        
        opcion = input("> ")
        helpers.clean_screen()
        
        if opcion == "1":
            print("Listando los clientes... \n")
            
            for cliente in db.Clientes.lista:
                print(cliente)
            

        elif opcion == "2":
            print("Buscando cliente...\n")
            
            dni = helpers.read_text(9, 9, "DNI (8 numeros y 1 letra)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado")


        elif opcion == "3":
            print("Añadiendo cliente...\n")
            
            dni = None
            while True:
                dni = helpers.read_text(9, 9, "DNI (8 numeros y 1 letra)").upper()
                if helpers.validate_dni(dni, db.Clientes.lista):
                    break
            
            nombre = helpers.read_text(2, 30, "Nombre (30 caracteres maximo)").capitalize()
            apellido = helpers.read_text(2, 30, "Apellido (30 caracteres maximo)").capitalize() #Primera letra en mayuscula
            db.Clientes.crear(dni, nombre, apellido)
            print(f" Cliente ({dni}, {nombre} {apellido}) añadido correctamente")

            
        elif opcion == "4":
            print("Modificando cliente...\n")
            
            dni = helpers.read_text(9, 9, "DNI (8 numeros y 1 letra)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.read_text(2, 30, f"Nombre (30 caracteres maximo [{cliente.nombre}])").capitalize()
                apellido = helpers.read_text(2, 30, f"Apellido (30 caracteres maximo [{cliente.apellido}])").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
            else:
                print("Cliente no encontrado")

        
        elif opcion == "5":
            print("Borrando un cliente...\n")
            
            dni = helpers.read_text(9, 9, "DNI (8 numeros y 1 letra)").upper()
            print("Cliente borrado correctamente.") if db.Clientes.borrar(dni) else print("Cliente no encontrado.")
                
        
        elif opcion == "6":
            print("Finalizando el sistema...\n")
            break
        
        input("\nPresiona ENTER para continuar")