# TO-DO-LIST

Este es un sencillo programa de línea de comandos escrito en Python que simula una lista de tareas por hacer (To-Do List). El programa permite a los usuarios gestionar sus tareas de manera interactiva a través de un menú de opciones.

## 📋 Funcionalidades Principales

El programa ofrece las siguientes opciones:

1.  **Agregar una tarea**: Permite al usuario ingresar una nueva tarea y añadirla a la lista.
2.  **Ver las tareas**: Muestra todas las tareas que han sido añadidas a la lista, con un identificador numérico para cada una.
3.  **Marcar una tarea como completada**: Guía al usuario a través de cada tarea para que pueda indicar si la ha completado. Al finalizar, muestra el estado de todas las tareas, marcando las completadas con una `[X]`.
4.  **Salir del programa**: Finaliza la ejecución del script.

## 🛠️ Estructura del Código

El programa está construido en un bucle principal `while` que se ejecuta hasta que el usuario elige la opción de salir (`0`). Se utiliza una función `menu_opciones()` para mostrar las opciones disponibles y una lista global `lista_tareas` para almacenar las tareas. El manejo de errores básicos está implementado con un bloque `try-except` para capturar entradas no numéricas.
