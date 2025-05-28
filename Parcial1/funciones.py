
def validar_notas(nota)->bool:
    """
Devuelve True si la nota está entre 1 y 10, sino False.
"""
    if nota >= 1 and nota <= 10:
        return True
    else:
        return False
#############################################################
def cargar_notas_alumnos():
    """
    Solicita al usuario que ingrese 5 notas válidas (entre 1 y 10) para un alumno.
    Cada nota es validada antes de guardarse. 
    Devuelve una lista con las 5 notas cargadas.
    """
    notas =[0]*5
    i = 0 #aca i es un contador
    while i <5 :
        nota = int(input(f"Ingresá la nota {i+1} del alumno (entre 1 y 10): "))
        if validar_notas(nota):
            notas[i] = nota
            i += 1
        else :
            print("la nota debe ser entre 1 y 10")
    return notas # se devuelven luego de cargar las 5 
#############################################################
def validar_nombre(nombre)->bool:

    for letra in nombre:
        if not ((letra >='a' and letra <='z') or (letra >='A' and letra <= 'Z')):
            return False
    return True
#############################################################
def cargar_nombres():
    while True:
        nombre = input("Ingresá el nombre del alumno: ")
        if validar_nombre(nombre):
            return nombre
        else:
            print(" El nombre solo puede contener letras. Intentá de nuevo.")
#############################################################
def validar_genero(genero)->bool:
    if genero =='F' or genero =='M' or genero =='X':
            return True
    else: 
        return False
#############################################################
def cargar_genero():
    while True:
        genero = input("Ingresá el genero del alumno (f / m/ x): ")
        if len(genero) ==1 and validar_genero(genero):
            return genero
        else:
            print("Error, Intentá de nuevo ")
#############################################################
def validar_legajo(legajo)->bool:
        if len(legajo) !=5:
            return False
        for i in range(len(legajo)):
            if legajo[i] <'0' or legajo[i]>'9': 
                return False
            
        return True
#############################################################
def cargar_legajo():
    while True: 
        legajo = input("Ingresá el legajo del alumno: (5 digitos) ")
        if validar_legajo(legajo):
            return legajo
        
        else: 
            print("Error, Intentá de nuevo ")
#############################################################
def pedir_cargar_datos(matriz_notas:list, lista_nombres:list, lista_generos:list, lista_legajos:list)->list:

    cantidad_alumnos_cargados =0 #contador 

    while cantidad_alumnos_cargados <30:
        print(f"cargar datos del alumno {cantidad_alumnos_cargados +1 }:")
#cargo las variables y valido 
        notas=cargar_notas_alumnos()
        nombre = cargar_nombres()
        genero =cargar_genero()
        legajo =cargar_legajo()
        
#guardo los datos en las listas 
        matriz_notas[cantidad_alumnos_cargados] = notas
        lista_nombres[cantidad_alumnos_cargados] = nombre
        lista_generos[cantidad_alumnos_cargados] = genero
        lista_legajos[cantidad_alumnos_cargados] = legajo

        cantidad_alumnos_cargados +=1

        if cantidad_alumnos_cargados <30: 
            continuar = input("¿seguir cargando alumnos? (si / no): ")
            if continuar == "no":
                break
        else:
            print("Se cargaron los 30 alumnos.")
##############################################################
def mostrar_un_alumno (posicion,lista_nombres, lista_generos, lista_legajos, matriz_notas):
    """ toma la posicion y los datos de cada lista y los imprime ordenados"""

    print(f"\nAlumno {posicion + 1}:")
    print(f"  Nombre : {lista_nombres[posicion]}")
    print(f"  Género : {lista_generos[posicion]}")
    print(f"  Legajo : {lista_legajos[posicion]}")
    print(f"  Notas  : {matriz_notas[posicion]}")
##############################################################
def mostrar_todoslos_datos_cargados (matriz_notas, lista_nombres, lista_generos, lista_legajos):
    """ toma los datos de la funcion que muestra los datos de mostrar_un_alumno
    tambien muestra todos """

    print("\n Listado de todos los alumnos cargados:")
    for i in range(len(lista_nombres)):
        if lista_nombres[i] != "":  # solo muestra si está cargado
            mostrar_un_alumno(i, lista_nombres, lista_generos, lista_legajos, matriz_notas)
##############################################################
#punto 3 
def calcular_promedios(matriz_notas:list)->list:
    """calcula el promedio de las notas que toma de la lista de matriz_notas 
    Devuelve una lista con el promedio de cada alumno en la misma posición 
    que el resto de los datos.
    """
    lista_promedios =[0]*len(matriz_notas) 

    for i in range(len(matriz_notas)):
        suma =0 #aculumula las notas 

        for j in range(5): #recorre una fila y sus 5 elementos 
            suma+= matriz_notas[i][j] 
        promedio=suma/5
        lista_promedios[i]=promedio
    return lista_promedios
##############################################################
def mostrar_menu()->int:

    print (" ◘ MENU DE OPCIONES ◘")
    print("1. Cargar Datos: Notas , Nombre Alumno , Genero , Legajo")
    print("2. Mostrar Datos Cargados")
    print("3. Calcular y Mostrar Promedio")
    print("4. Ordenar Promedio por alumno")
    print("5. Materia/s con mayor promedio general.")
    print("6. Buscar por legajo")
    print("7. Matriz Cantidad de Notas")
    print("8. Salir")

    opcion = input("Elija una opción (1-8): ")
    return int(opcion)
#############################################################
#punto 4
def ordenar_por_promedio_desc(lista_promedios, lista_nombres, lista_generos, lista_legajos, matriz_notas):

    for i in range(0, len(lista_promedios) - 1, 1):
        for j in range(i + 1, len(lista_promedios)):
            if lista_promedios[i] < lista_promedios[j]:
                # Intercambiar promedios
                aux = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = aux

                # Intercambiar nombres
                aux = lista_nombres[i]
                lista_nombres[i] = lista_nombres[j]
                lista_nombres[j] = aux

                # Intercambiar géneros
                aux = lista_generos[i]
                lista_generos[i] = lista_generos[j]
                lista_generos[j] = aux

                # Intercambiar legajos
                aux = lista_legajos[i]
                lista_legajos[i] = lista_legajos[j]
                lista_legajos[j] = aux

                # Intercambiar notas
                aux = matriz_notas[i]
                matriz_notas[i] = matriz_notas[j]
                matriz_notas[j] = aux
#############################################################
#punto5
def calcular_promedios_por_materia(matriz_notas: list) -> list:
    """Devuelve una lista con el promedio de cada materia"""
    promedios_materias = [0] * 5

    for j in range(5):  # columnas 
        suma = 0
        for i in range(len(matriz_notas)):  # filas
            suma += matriz_notas[i][j]
        promedio = suma / len(matriz_notas)
        promedios_materias[j] = promedio

    return promedios_materias #lista de prom uno por materia
#############################################################
#Punto 6 (legajo)
def buscar_posicion(legajo_buscado: str, lista_legajos: list) -> int:
    """Devuelve la posición del legajo si se encuentra, o -1 si no existe"""
    i = 0
    while i < len(lista_legajos):
        if lista_legajos[i] == legajo_buscado:
            return i
        i += 1
    return -1
#############################################################

def mostrar_datos_por_posicion(posicion: int, lista_nombres: list, lista_generos: list, lista_legajos: list, matriz_notas: list, lista_promedios: list):
    """Muestra los datos completos de un alumno por su posición"""
    print("\nDatos del alumno:")
    mostrar_un_alumno (posicion,lista_nombres, lista_generos, lista_legajos, matriz_notas)
    print(f"  Promedio: {lista_promedios[posicion]:.2f}")

#############################################################
def mostrar_materia_con_mayor_promedio(matriz_notas: list):
    promedios = calcular_promedios_por_materia(matriz_notas)

    # Encontrar el mayor promedio manualmente
    mayor_prom = promedios[0]
    i = 1
    while i < len(promedios):
        if promedios[i] > mayor_prom:
            mayor_prom = promedios[i]
        i += 1
    # Mostrar materias que tienen ese mayor promedio
    print("\nMateria/s con mayor promedio general:")
    j = 0
    while j < len(promedios):
        if promedios[j] == mayor_prom:
            print(f"MATERIA_{j+1} - Promedio: {mayor_prom:.2f}")
        j += 1

#############################################################
#punto 7 
def contar_notas_por_materia(matriz_notas: list, numero_materia: int) -> list:
    """ recibo una matriz y un numero de posicion(-1), y devuelve una nueva matriz
    realiza un ciclo de recorrido repetitivo """
    matriz_cantidad_notas = [0] * 10 # lista de 10 pos 
    columna = numero_materia - 1  

    i = 0
    while i < len(matriz_notas):  # recorrer alumnos
        nota = matriz_notas[i][columna]  # nota del alumno i en materia
        if nota >= 1 and nota <= 10:
            matriz_cantidad_notas[nota - 1] += 1
        i += 1

    return matriz_cantidad_notas

