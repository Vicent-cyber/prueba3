TIPOPAQUETE = ["pequeño", "mediano", "grande"]

def Registrar_Pedido(pedidos):
    print("")
    nombreApellido = input("Nombre y apellido: ")
    direccion = input("Dirección: ")
    sector = input("Sector: ")
    detallePedido = input("Detalle del pedido(Pequeño¬Mediano¬Grande): ").lower()
    while detallePedido is not TIPOPAQUETE:
        print("Opción no válida, considere las opciones")
        detallePedido = input("Detalle del pedido(Pequeño¬Mediano¬Grande): ").lower()
    if detallePedido == "pequeño":
        cantidadPedidoP = int(input("¿Cuántos pequeño desea?: "))
    elif detallePedido == "mediano":
        cantidadPedidoM = int(input("¿Cuántos mediano desea?: "))
    elif detallePedido == "grande":
        cantidadPedidoG = int(input("¿Cuántos grande desea?: "))

    pedidos = ({
        "Cliente:" ,nombreApellido,
        "Dirección:" ,direccion,
        "Sector:" ,sector,
        "Paquetes:" "Pequeño:" ,cantidadPedidoP, "Mediano:" ,cantidadPedidoM, "Grande:" ,cantidadPedidoG
    })

def listarPedido(pedidos): 
    for i in pedidos:
        print(pedidos)

def imprimirHojaRuta(pedidos):
    sectorOpcion = input("Sector: ").lower()
    while sectorOpcion is not TIPOPAQUETE:
        print("Opción no válida, considere las opciones")
        sectorOpcion = input("Detalle del pedido(Pequeño¬Mediano¬Grande): ").lower()

    if sectorOpcion in TIPOPAQUETE:
        pedidos_imprimir = []
        for i in pedidos:
            if i ["pequeño"] == sectorOpcion:
                pedidos_imprimir.append(pedidos)
            elif i ["mediano"] == sectorOpcion:
                pedidos_imprimir.append(pedidos)
            elif i ["grande"] == sectorOpcion:
                pedidos_imprimir.append(pedidos)
        imprimirPedidos = f"Hoja_de_ruta_de_{sectorOpcion}.txt"

    with open(imprimirPedidos, "w") as archivo:
        for pedidos in pedidos_imprimir:
            archivo.write