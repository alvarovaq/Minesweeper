# Minesweeper
Encuentra las minas ocultas sin que exploten. Clásico juego de buscaminas en el que cada casilla muestra un número con la cantidad de minas que se encuentran alrededor. Los números indican el número de minas que hay en las casillas adyacentes.


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

## Vídeos

Aunque este juego es muy conocido a nivel internacional, podeis ver en el siguiente vídeo un poco el funcionamiento del mismo. En la aplicación utilizo sonidos cuando el jugador pulsa una casilla para indicar de una manera más dinámica si la casilla no hay peligro, o por lo contrario hay una mina y ha perdido el juego. Podeís activar el volumen para comprobarlo.

https://user-images.githubusercontent.com/113897176/198708445-a15ab4e1-5e8f-49cc-a20f-517f6c165d65.mp4

## Desarrollo

*Diciembre de 2020 - 2 Semanas*

Este juego ha sido desarrollado por mí con la motivación de poder recreear el famoso juego del busca minas. Es un juego en la cual es muy común y muy usado para aprender no solo un lenguaje de programación en específico, si no que también para aprender a desarrollar la lógica de programación, y así ha sido.

Ha sido un proyecto bastante entretenido y curioso, no solo por la lógica del juego, sino que tambíen a la hora de programar la interfaz.

## Paquetes

*  pygame

Ejecuta el siguiente comando para instalarlos

`$ pip install -r requirements.txt`
o bien
`$ pip install pygame`

Ejecuta el archivo *main.py* para iniciar el juego

`$ python main.py`

## Contacto

* Email: alvaro.vaquero.tel@gmail.com
* LinkedIn: https://www.linkedin.com/in/alvaro-vaquero-gimenez/
* Twitter: https://twitter.com/AlvaroVaqGim
* Página Web: https://alvarovaq.github.io
