
def validar_texto(lista: list) -> list:
    for i in range(len(lista)):
        while True:
                lista[i] = int (input(f"Nota {i+1}: "))
                if lista[i] >=1 and lista[i] <=10:
                    break
                else:
                    print("La nota debe ser entre 1 y 10 ")
    return lista
#############################################################
def mostrar_datos(lista_a:list, lista_b:list, lista_c:list, lista_d:list) -> None:

    """
    Muestra los elementos de tres listas alineados en columnas 
    Cada elemento en la misma posición representa un conjunto de datos relacionados (nombre, edad y nota)
    Si el texto de lista_a en la posición actual tiene menos de 8 caracteres, 
    se agrega una tabulación extra para mantener el formato visual alineado.

    Args:
        lista_a (list): Lista de textos (por ejemplo, genero o códigos).
        lista_b (list): Lista de datos relacionados (por ejemplo, edades).
        lista_c (list): Lista de datos relacionados (por ejemplo, notas o valores).
    
    Returns:
        None: Esta función solo imprime los datos, no devuelve ningún valor.

    """
    for i in range(len(lista_a)):
        if ((len(lista_a[i]) >1 and len(lista_a[i]) <8 ) and (len(lista_b[i]) >1 and len(lista_b[i]) <8 )) or ((len(lista_a[i])>1 and len(lista_a[i]) <8) and len(lista_b[i]) <8):
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t\t{lista_c[i]}\t\t{lista_d[i]}") 
        if ((len(lista_a[i]) >1 and len(lista_a[i]) <8 ) and (len(lista_b[i]) >1 and len(lista_b[i]) <8 )) or ((len(lista_a[i])>1 and len(lista_a[i]) <8) and len(lista_b[i]) <8):
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t\t{lista_c[i]}\t\t{lista_d[i]}") 
    for i in range(len(lista_a)):
        if ((len(lista_a[i]) >1 and len(lista_a[i]) <8 ) and (len(lista_b[i]) >1 and len(lista_b[i]) <8 )) or ((len(lista_a[i])>1 and len(lista_a[i]) <8) and len(lista_b[i]) <8):
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t\t{lista_c[i]}\t\t{lista_d[i]}") 
        elif len(lista_a[i]) >=8 and len(lista_b[i]) <=8:
            print(f"{lista_a[i]}\t{lista_b[i]}\t\t{lista_c[i]}\t\t{lista_d[i]}")
        elif len(lista_a[i]) <=8 and len(lista_b[i]) >=8:
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}\t\t{lista_d[i]}")
        elif len(lista_a[i]) >=8 and len(lista_b[i]) >=14:
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}\t\t{lista_d[i]}")                 
        else:
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}\\t\t{lista_d[i]}")   
#############################################################
def copiar_lista(lista_a:list, lista_b:list)->list:
    """Copia el contenido de dos listas (lista_a y lista_b) en nuevas listas independientes.
    Parámetros:
        lista_a : list
            Lista de origen, por ejemplo nombres
        lista_b : list
            Segunda lista de origen, por ejemplo, edades
    Retorna:
    (nombres_originales, edades_originales)
    Dos listas nuevas que contienen copias de los valores de lista_a y lista_b
    respectivamente. No modifica las listas originales
    """
    nombres_originales = [-1] * len(lista_a) # crea un -1 en cada posicion de lista_a
    edades_originales = [-1] * len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i] = lista_a[i]
        edades_originales[i] = lista_b[i]

        return nombres_originales, edades_originales
#############################################################
def orden_ascendente(lista_a:list, lista_b:list, lista_c:list) -> list:

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if lista_c[i] > lista_c[j]:
            
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] > lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar
#############################################################
def menu_opciones():
    """ va a recibir las variables de opciones a """
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Cargar Datos: Notas , Nombre Alumno , Genero , Legajo")
        print("2. Mostrar Datos Cargados")
        print("3. Mostrar Promedio")
        print("4. Promedio por alumno")
        print("5. Nota más alta")
        print("6. Nota más baja")
        print("7. Salir")

        opcion = input("Elija una opción (1-7): ")

        match opcion:
            case "1":
                print(">> Cargando notas...")
            case "2":
                print(">> Mostrando matriz...")
            case "3":
                print(">> Calculando promedio general...")
            case "4":
                print(">> Calculando promedio por alumno...")
            case "5":
                print(">> Buscando nota más alta...")
            case "6":
                print(">> Buscando nota más baja...")
            case "7":
                print(">> Saliendo del programa. ¡Gracias!")
                break
            case _:
                print(">> Opción inválida. Intentá de nuevo.")
#############################################################
def validar_notas(nota)->bool:
    if nota >= 1 and nota <= 10:
        return True
    else:
        return False
#############################################################
def cargar_notas_alumnos():
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
    if genero =='f' or genero =='m' or genero =='x':
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
def pedir_cargar_datos(matriz_notas:list, nombres:list, generos:list, legajos:list)->list:  

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
        nombres[cantidad_alumnos_cargados] = nombre
        generos[cantidad_alumnos_cargados] = genero
        legajos[cantidad_alumnos_cargados] = legajo

        cantidad_alumnos_cargados +=1

        if cantidad_alumnos_cargados <30: 
            continuar = input("¿seguir cargando alumnos? (si / no): ")
            if continuar == "no":
                break
        else:
            print("Se cargaron los 30 alumnos.")
