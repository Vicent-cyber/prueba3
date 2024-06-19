import funciones as fn
pedidos = []

while True: 
    print("Bienvenido a PaquExpress")
    print("========================")
    print("1. Registrar pedido     ")
    print("2. Listar los todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa   ")
    opcion = int(input("Ingrese opción: "))
    
    if opcion == 1:
        fn.Registrar_Pedido
        print("")
    elif opcion == 2:
        fn.listarPedido
    elif opcion == 3:
        fn.imprimirHojaRuta
    elif opcion == 4:
        print("")
        print("¡Gracias por preferirnos!..")
        break
    else:
        print("Opción no válida")
