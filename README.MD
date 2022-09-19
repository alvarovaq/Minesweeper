# Minesweeper
Encuentra las minas ocultas sin que exploten. Clásico juego de buscaminas en el que cada casilla muestra un número con la cantidad de minas que se encuentran alrededor. Pulsa sobre una casilla cualquiera del tablero para iniciar el juego. Los números indican el número de minas que hay en las casillas adyacentes.


<img src="https://user-images.githubusercontent.com/113897176/191001273-596a29a4-30df-4560-909c-4c364bed8750.png" width="300">

## Instrucciones
Comienzas con un tablero formado por una cuadrícula dónde algunas de sus celdas contienen minas. El objetivo es descubrir todas las casillas que no contienen minas. Si abrimos una casilla que contiene una mina, hemos perdido la partida. Si se descubre una celda que no contiene minas, esta mostrará un número indicando cuantas minas hay en las 8 casillas que la rodean. Las casillas sin minas de alrededor se abrirán automáticamente al hacer clic sobre ellas.

Puedes colocar una bandera sobre una casilla, en la que consideres que hay una mina, haciendo clic con el botón derecho.

Si quieres salir de la partida, pulsa la tecla ESC. En caso de salir, no se guardará la partida.
En la pantalla se encuentra dos marcadores, uno marca el tiempo que ha trascurrido desde el inicio de la partida, y la segunda indican las banderas restantes.
Estos marcadores se pueden desplazar haciendo clic con el botón izquierdo y deplazandolo hasta la posición deseada.

## Niveles

|           | Dimensiones     | Minas  |
| ----------|:---------:|------:|
| Fácil  | 8x8 | 10 |
| Medio  | 14x14 | 40 |
| Difícil  | 20x20 | 99 |

## Ejecución

Para ejecutar dicho juego, es imprescidible tener instalado en el ordenador las siguientes librerias
1.  pygame

Ejecutar archivo *main.py*
