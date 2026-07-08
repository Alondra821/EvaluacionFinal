planes = {
    "F001": ["Plan Básico", "mensual", 1, False, False, "libre"],
    "F002": ["Plan Full", "mensual", 1, True, True, "libre"],
    "F003": ["Plan Estudiante", "trimestral", 3, False, True, "tarde"],
    "F004": ["Plan Senior", "trimestral", 3, True, False, "mañana"],
    "F005": ["Plan Anual Pro", "anual", 12, True, True, "libre"],
    "F006": ["Plan Nocturno", "mensual", 1, False, True, "noche"]
}

inscripciones = {
    "F001": [14990, 30],
    "F002": [22990, 10],
    "F003": [39990, 0],
    "F004": [35990, 6],
    "F005": [159990, 2],
    "F006": [18990, 15]
}

def cupos_tipo(tipo):
    total = 0

    for codigo in planes:
        if planes[codigo][1].lower() == tipo.lower():
            total += inscripciones[codigo][1]

    print("El total de cupos disponibles es:", total)
    
while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        tipo = input("Ingrese tipo de plan a consultar: ")
        cupos_tipo(tipo)

    elif opcion == "2":
        pass

    elif opcion == "3":
        pass

    elif opcion == "4":
        pass

    elif opcion == "5":
        pass

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Debe seleccionar una opción válida")