"""
LISTA DE TAREAS POR HACER (TO-Do-List)
Estructura Básica del Programa:

Tu programa necesitará realizar las siguientes acciones principales:

1. Mostrar el menú de opciones: Al usuario se le presentarán las acciones que puede realizar (agregar tarea, ver tareas, marcar como completada, salir).
2. Agregar una tarea: Pedir al usuario que ingrese la descripción de la nueva tarea y añadirla a una lista.
3. Ver las tareas: Mostrar la lista de tareas, posiblemente con un índice para identificarlas.
4. Marcar una tarea como completada: Pedir al usuario el índice de la tarea a completar y actualizar su estado.
5. Salir del programa: Terminar la ejecución.
"""

# defino mi menu como una funcion
def menu_opciones():
    print("BIENVENIDO AL MENU TO-DO-LIST")
    print("1. Agregar una tarea")
    print("2. Ver las tareas")
    print("3. Marcar una tarea como completada")
    print("0. Salir del programa")


# Inicializamos con un valor que no sea 0 para que el bucle empiece
op = -1

# Defino una lista como variable global ya que se usara en diferentes partes del codigo
lista_tareas = []

print("\t\t ***** TO-DO-LIST ***** ")
while(op):
    print() # salto de linea
    menu_opciones()
    print() # salto de linea

    try:
        # pedimos al usuario que elija una opcion del menu
        op = int(input("Elija una opción: "))
    except ValueError: # esto se ejecuta en caso el usuario ingrese un valor no numerico
        print("Entrada inválida. Por favor, ingresa un número.")
        op = -1 # Para asegurar que el bucle continúe en caso de error

    if op == 1:
        tarea = input("Ingrese la tarea que desee agregar a su lista: ")
        lista_tareas.append(tarea)

    elif op == 2:
        # cuando existe por lo menos una tarea en la lista
        if len(lista_tareas) > 0:
            print("\tLISTA DE TAREAS.")
            for id, tarea in enumerate(lista_tareas):
                print(f"-> Tarea {id+1}: {tarea}")
                
        # cuando la lista esta vacia
        else:
            print("Aún no se agrega una tarea.")

    elif op == 3:
        if len(lista_tareas) > 0:
            # creamos una nueva lista para analizar el estado de cada tarea
            estado_de_tareas = []

            for id, analizar_tarea in enumerate(lista_tareas):
                # internamente el usuario va analizar cada tarea y se preguntara si ya esta terminada o no

                # preguntamos al usuario si la tarea esta terminada. 
                # la funcion lower convertira la palabra en minusculas
                print(f"Analizamos la tarea {id+1}: {analizar_tarea}")
                tarea_completada = input("¿La tarea esta terminada?(si/no)").lower() 
                    
                # verificamos la respuesta del usuario
                if tarea_completada == "si":
                    # agregamos esa tarea a mi lista estado_de_tareas y la marcamos como completada
                    estado_de_tareas.append(f"{analizar_tarea} [X]")
                    print("¡Excelente! Tarea marcada como terminada.\n")
                else:
                    # agregamos esa tarea actual que se analizo, pero no la marcamos xq aun esta pendiente
                    estado_de_tareas.append(f"{analizar_tarea} [ ]")
                    print("Tarea pendiente.\n")
                    
            # despues de analizar cada tarea, ya podemos mostrar el estado actual de cada tarea
            print("\n\tESTADO DE LA LISTA DE TAREAS")
            for id_tarea_estado in range(0, len(estado_de_tareas)):
                print(f"-> Tarea {id_tarea_estado+1}: {estado_de_tareas[id_tarea_estado]}")
                
        else:
            print("Aun no se ha agregado ninguna tarea.")
    
    elif op >= 4:
        print("Opcion no existente en el menu de opciones.")
    
print("Fin del BUCLE")
