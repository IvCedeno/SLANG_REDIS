import redis

conn = redis.Redis(host='localhost', port=6379, db=0)

def agregarPalabra(palabra, significado):
    if conn.exists(palabra) == 0:
        conn.set(palabra, significado)
        print("Palabra agregada!\n")
    else:
        print("La palabra ya existe en el diccionario!\n")

def editarPalabra(palabra, significado):
    if conn.exists(palabra) == 1:
        conn.set(palabra, significado)
        print("Palabra actualizada!\n")
    else:
        print("La palabra no existe en el diccionario!\n")

def eliminarPalabra(palabra):
    if conn.exists(palabra) == 1:
        conn.delete(palabra)
        print("Palabra eliminada!\n")
    else:
        print("La palabra no existe en el diccionario!\n")
    
def listarPalabras():
    palabras = conn.keys()
    for p in palabras:
        palabra = str(p)
        significado = str(conn.get(p))
        print("- " + palabra[2:len(palabra) - 1] + ": " + significado[2:len(significado) - 1] + "\n")

def buscarPalabra(palabra):
    if conn.exists(palabra) == 1:
        p = conn.get(palabra)
        significado = str(p)
        print("- " + palabra + ": " + significado[2:len(significado) - 1] + "\n")
    else:
        print("La palabra no existe en el diccionario!\n")


while True:
    print("Seleccione una opcion:")
    print("1. Agregar nueva palabra")
    print("2. Editar palabra existente")
    print("3. Eliminar palabra existente")
    print("4. Ver listado de palabras")
    print("5. Buscar significado de palabra")
    print("6. Salir")
    opcion = int(input())

    if opcion == 1:
        print("\nAgregar nueva palabra")
        palabra = input("Nueva palabra: ")
        significado = input("Significado: ")
        agregarPalabra(palabra, significado)
    elif opcion == 2:
        print("\nEditar palabra existente")
        palabra = input("Palabra: ")
        significado = input("Nuevo significado: ")
        editarPalabra(palabra, significado)
    elif opcion == 3:
        print("\nEliminar palabra existente")
        palabra = input("Palabra: ")
        eliminarPalabra(palabra)
    elif opcion == 4:
        print("\nListado de palabras")
        listarPalabras()
        print()
    elif opcion == 5:
        print("\nBuscar significado de palabra")
        palabra = input("Palabra: ")
        buscarPalabra(palabra)
    elif opcion == 6:
        print("\nHasta la proxima!!\n")
        break
    else:
        print("\nOpcion invalida! Intente nuevamente\n")