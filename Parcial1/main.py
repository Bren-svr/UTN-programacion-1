from funciones import*



## Programa principal 

matriz_notas = [[0]*5 for _ in range(30)]
lista_nombres = [""] * 30
lista_generos = [""] * 30
lista_legajos = [""] * 30
contador_de_ingresos = 0 
continuar = "si" 
datos_cargados =False # bandera de datos empieza en false porque no hay datos cargados (punto que dice que no se muestren los datos si no hay nada cargado)
lista_promedios = [0] * 30

##
matriz_notas = [
    [7, 5, 9, 6, 8], [10, 4, 6, 7, 8], [3, 6, 7, 5, 9], [4, 8, 10, 6, 5], [6, 7, 9, 3, 10],
    [9, 5, 7, 6, 8], [8, 6, 10, 9, 4], [7, 8, 5, 6, 10], [10, 9, 8, 7, 6], [5, 4, 6, 7, 9],
    [6, 5, 4, 8, 10], [7, 9, 10, 6, 5], [3, 5, 7, 8, 6], [10, 10, 10, 9, 8], [8, 7, 6, 5, 4],
    [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8], [3, 4, 5, 6, 7], [2, 3, 4, 5, 6],
    [9, 8, 7, 6, 5], [10, 9, 8, 7, 6], [6, 7, 8, 9, 10], [5, 6, 7, 8, 9], [4, 5, 6, 7, 8],
    [3, 4, 5, 6, 7], [2, 3, 4, 5, 6], [1, 2, 3, 4, 5], [10, 10, 9, 8, 7], [6, 6, 6, 5, 4]]

lista_nombres = [
    "Ana", "Benjamín", "Carla", "Damián", "Elena", "Facundo", "Gabriela", "Hernán", "Inés", "Julián",
    "Karina", "Luis", "Mariana", "Nicolás", "Olivia", "Pablo", "Gabriel", "Rodrigo", "Sofía", "Tomás",
    "Ursula", "Franco", "Wanda", "Javier", "Yamila", "Zulma", "Alma", "Bruno", "Camila", "Diego"]

lista_generos = [
    "F", "M", "F", "M", "F", "M", "F", "M", "F", "M",
    "F", "M", "F", "M", "F", "M", "X", "M", "F", "M",
    "F", "M", "F", "M", "F", "M", "F", "M", "F", "M"]

lista_legajos = [
    "10001", "10002", "10003", "10004", "10005",
    "10006", "10007", "10008", "10009", "10010",
    "10011", "10012", "10013", "10014", "10015",
    "10016", "10017", "10018", "10019", "10020",
    "10021", "10022", "10023", "10024", "10025",
    "10026", "10027", "10028", "10029", "10030"]

datos_cargados = True  
##
while True:
    opcion = mostrar_menu()

    match opcion:
        case 1:

            pedir_cargar_datos(matriz_notas ,lista_nombres, lista_generos, lista_legajos)
            datos_cargados =True

        case 2:
            if datos_cargados ==True:
                mostrar_todoslos_datos_cargados(matriz_notas ,lista_nombres, lista_generos, lista_legajos)
            else:
                print("Primero debés cargar los datos con la opción 1.\n")
        
        case 3:
            if datos_cargados ==True:
                promedios_notas= calcular_promedios(matriz_notas)
                print("\n Promedios de los alumnos:")
                for i in range(len(promedios_notas)):
                    if lista_nombres[i] != "":
                        print(f"{lista_nombres[i]} - Promedio: {promedios_notas[i]}")
            else:
                print("\n Primero debés cargar los datos con la opción 1.\n")

        case 4: # Punto Ordenar y mostrar los datos de los estudiantes por promedio de manera DESC.
            if datos_cargados ==True:
                lista_promedios = calcular_promedios(matriz_notas)
                ordenar_por_promedio_desc(lista_promedios, lista_nombres, lista_generos, lista_legajos, matriz_notas)
                print("Alumnos ordenados por promedio (mayor a menor):")

                for i in range(len(lista_promedios)):
                    if lista_nombres[i] != "":
                        print(f"{lista_nombres[i]} - Promedio: {lista_promedios[i]}")
            else:
                print("Primero debés cargar los datos con la opción 1.\n")

        case 5: #Mostrar la/s materia/s con mayor promedio general. 
            if datos_cargados ==True:
                mostrar_materia_con_mayor_promedio(matriz_notas)
            else:
                print("Primero debés cargar los datos con la opción 1.\n")

        case 6: #Buscar y mostrar todos los datos de un estudiante por legajo
            if datos_cargados == True:
                legajo_buscado = cargar_legajo()
                lista_promedios = calcular_promedios(matriz_notas)
                posicion = buscar_posicion(legajo_buscado, lista_legajos)

                if posicion != -1:
                    mostrar_datos_por_posicion(posicion, lista_nombres, lista_generos, lista_legajos, matriz_notas, lista_promedios)
                else:
                    print(" Legajo no encontrado.")
            else:
                print("Primero debés cargar los datos con la opción 1.")
            

        case 7:#
            if datos_cargados == True: 
                numero_materia = int(input("Ingresar el numero de materia a consultar: "))
                conteo= contar_notas_por_materia(matriz_notas,numero_materia)
                print(f"\nRecuento de notas para la materia {numero_materia}:")
                for i in range(10):
                    print(f"Nota {i+1}: {conteo[i]} veces")
            else:
                print("Primero debés cargar los datos con la opción 1.\n")

        case 8:
            print(" Programa finalizado.")
            break

        case _:
            print(" Opción inválida. Elegí entre 1 y 7.\n")

