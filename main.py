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


def busqueda_precio(p_min, p_max):
    encontrados = []

    for codigo in inscripciones:
        precio = inscripciones[codigo][0]
        cupos = inscripciones[codigo][1]

        if precio >= p_min and precio <= p_max and cupos != 0:
            nombre = planes[codigo][0]
            encontrados.append(nombre + "--" + codigo)

    encontrados.sort()

    if len(encontrados) == 0:
        print("No hay planes en ese rango de precios.")
    else:
        print("Los planes encontrados son:", encontrados)


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
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))

            busqueda_precio(p_min, p_max)

        except ValueError:
            print("Ingrese valores numéricos.")


    elif opcion == "3":
        codigo = input("Ingrese código del plan a actualizar: ").upper()

        if codigo in inscripciones:
            nuevo_precio = int(input("Ingrese nuevo precio: "))

            inscripciones[codigo][0] = nuevo_precio

            print("Precio actualizado correctamente.")
        else:
            print("El código del plan no existe.")


    elif opcion == "4":
        codigo = input("Ingrese código del nuevo plan: ").upper()

        if codigo in planes:
            print("El código ya existe.")

        else:
            nombre = input("Ingrese nombre del plan: ")
            tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
            duracion = int(input("Ingrese duración en meses: "))

            clases = input("¿Incluye clases? (True/False): ").lower() == "true"
            entrenador = input("¿Incluye entrenador? (True/False): ").lower() == "true"
            horario = input("Ingrese horario: ")

            precio = int(input("Ingrese precio: "))
            cupos = int(input("Ingrese cupos disponibles: "))

            planes[codigo] = [nombre, tipo, duracion, clases, entrenador, horario]
            inscripciones[codigo] = [precio, cupos]

            print("Plan agregado correctamente.")


    elif opcion == "5":
        codigo = input("Ingrese código del plan a eliminar: ").upper()

        if codigo in planes:
            del planes[codigo]
            del inscripciones[codigo]

            print("Plan eliminado correctamente.")
        else:
            print("El código del plan no existe.")


    elif opcion == "6":
        print("Programa finalizado.")
        break


    else:
        print("Debe seleccionar una opción válida.")