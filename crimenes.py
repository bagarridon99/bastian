import json

"""with open("crime_history.json",mode="r") as lecturaJson:
    leerJson = json.load(lecturaJson)
    for person in leerJson:
       print(person["rut"])

       
def eliminarInfo():
    # Solicitar al usuario que ingrese el RUT y el tipo
    rut = input("Ingrese el RUT: ")
    tipo = input("Ingrese el tipo de delito: ")
    
    # Leer el archivo JSON
    with open("crime_history.json", "r") as archivo:
        data = json.load(archivo)
    
    # Filtrar la lista para eliminar la entrada correspondiente
    data_filtrada = [persona for persona in data if not (persona["rut"] == rut and persona["tipo"] == tipo)]
    
    # Escribir los datos filtrados de nuevo en el archivo JSON
    with open("crime_history.json", "w", encoding="utf-8") as archivo:
        json.dump(data_filtrada, archivo, indent=4, ensure_ascii=False)
    
    # Confirmación
    print(f"Entrada con RUT {rut} y tipo '{tipo}' ha sido eliminada.")

# Llamar a la función para eliminar la información
eliminarInfo()




def agregarInfo():
    # Solicitar al usuario que ingrese el RUT, tipo de delito y descripción
    rut = input("Ingrese el RUT: ")
    tipo = input("Ingrese el tipo de delito: ")
    descripcion = input("Ingrese la descripción: ")
    
    # Crear una nueva entrada
    nueva_entrada = {
        "rut": rut,
        "tipo": tipo,
        "descripcion": descripcion
    }
    
    # Leer el archivo JSON
    with open("crime_history.json", "r") as archivo:
        data = json.load(archivo)
        
    # Agregar la nueva entrada a los datos existentes
    data.append(nueva_entrada)
    
    # Escribir los datos actualizados de nuevo en el archivo JSON
    with open("crime_history.json", "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)
    
    # Confirmación
    print(f"Nueva entrada con RUT {rut}, tipo '{tipo}' y descripción '{descripcion}' ha sido agregada.")

# Llamar a la función para agregar la información
agregarInfo()"""""


"""def mostrarInfo():
    # Leer el archivo JSON
    with open("crime_history.json", "r") as archivo:
        data = json.load(archivo)
    
    # Mostrar la información de manera ordenada y legible
    print("Información de criminales:")
    print("--------------------------")
    for persona in data:
        print(f"RUT: {persona['rut']}")
        print(f"Tipo: {persona['tipo']}")
        print(f"Descripción: {persona['descripcion']}")
        print("--------------------------")

# Llamar a la función para mostrar la información
mostrarInfo()"""



"""def buscarHistorial():
    # Leer el archivo JSON
    with open("crime_history.json", "r") as archivo:
        data = json.load(archivo)
    
    # Ingreso manual del RUT
    rut = input("Ingresa el RUT de la persona para buscar su historial de delitos: ")
    
    # Variable para contar los delitos encontrados
    delitos_encontrados = False
    
    # Mostrar historial de delitos para el RUT especificado
    for persona in data:
        if persona['rut'] == rut:
            if not delitos_encontrados:
                print(f"Historial de delitos para RUT {rut}:")
                print("--------------------------")
                delitos_encontrados = True
            
            print(f"Tipo de delito: {persona['tipo']}")
            print(f"Descripción: {persona['descripcion']}")
            print("--------------------------")
    
    if not delitos_encontrados:
        print(f"No se encontró información para el RUT {rut}.")

# Ejemplo de uso: buscar historial para un RUT ingresado manualmente
buscarHistorial()"""




"""def añadirDelito():
    # Leer el archivo JSON
    with open("crime_history.json", "r") as archivo:
        data = json.load(archivo)
    
    # Ingreso manual de los datos del nuevo delito
    rut = input("Ingresa el RUT de la persona a la que deseas añadir un nuevo delito: ")
    tipo = input("Ingresa el tipo de delito: ")
    descripcion = input("Ingresa la descripción del delito: ")
    
    # Crear nuevo registro de delito
    nuevo_delito = {
        "rut": rut,
        "tipo": tipo,
        "descripcion": descripcion
    }
    
    # Añadir el nuevo delito a la lista de delitos existente
    data.append(nuevo_delito)
    
    # Escribir los datos actualizados de vuelta al archivo JSON
    with open("crime_history.json", "w") as archivo:
        json.dump(data, archivo, indent=4)
    
    print(f"Se ha añadido correctamente el delito al historial de {rut}.")

# Ejemplo de uso: añadir un nuevo delito al historial
añadirDelito()"""




"""def generarReporte(opcion):
    # Leer el archivo JSON
    with open("crime_history.json", "r") as archivo:
        data = json.load(archivo)
    
    reporte = []  # Lista para almacenar los datos del reporte
    
    if opcion == 1:
        # Reporte de todos los delitos registrados
        for delito in data:
            reporte.append({
                "rut": delito['rut'],
                "tipo_delito": delito['tipo'],
                "descripcion": delito['descripcion']
            })
    
    elif opcion == 2:
        # Reporte de delitos por tipo
        tipos_delitos = set([delito['tipo'] for delito in data])
        for tipo in tipos_delitos:
            delitos_tipo = []
            for delito in data:
                if delito['tipo'] == tipo:
                    delitos_tipo.append({
                        "rut": delito['rut'],
                        "descripcion": delito['descripcion']
                    })
            reporte.append({
                "tipo_delito": tipo,
                "delitos": delitos_tipo
            })
    
    elif opcion == 3:
        # Reporte de delitos por persona (RUT)
        rut = input("Ingresa el RUT de la persona para generar el reporte de sus delitos: ")
        delitos_persona = []
        for delito in data:
            if delito['rut'] == rut:
                delitos_persona.append({
                    "tipo_delito": delito['tipo'],
                    "descripcion": delito['descripcion']
                })
        reporte.append({
            "rut": rut,
            "delitos": delitos_persona
        })
    
    else:
        print("Opción no válida. Por favor ingresa una opción válida.")
        return
    
    # Guardar el reporte en un archivo JSON
    with open("reporte.json", "w") as outfile:
        json.dump(reporte, outfile, indent=4)
    
    print(f"Reporte generado y guardado en 'reporte.json' satisfactoriamente.")

# Ejemplo de uso
print("1. Reporte de Todos los Delitos Registrados")
print("2. Reporte de Delitos por Tipo")
print("3. Reporte de Delitos por Persona (RUT)")
opcion = int(input("Selecciona el tipo de reporte que deseas generar (1, 2 o 3): "))
generarReporte(opcion)"""




