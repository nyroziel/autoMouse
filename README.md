# NO TE QUEDES AFK :)

Este script en Python mueve el cursor del ratón de forma automática para evitar que tu computadora se quede en estado de inactividad (AFK). También permite pausar y reanudar el movimiento del ratón con la tecla 'p' y detener el programa completamente con la tecla 'q'.

## Requisitos

- Python 3.x
- Librerías Python: `pyautogui`, `keyboard`, `threading`

Puedes instalar las librerías necesarias con el siguiente comando:

# Cómo funciona
El script realiza los siguientes pasos:

Imprime mensajes de bienvenida e instrucciones en la consola.
Configura los eventos necesarios para detener (stop_event) y pausar/reanudar (pause_event) el programa.
Inicia un hilo (mover_mouse) que mueve el ratón cada 10 segundos entre dos posiciones.
Inicia un segundo hilo (esperar_tecla) que espera a que se presionen las teclas q o p para detener o pausar/reanudar el programa, respectivamente.
El ratón se moverá hacia la derecha y presionará la tecla space cada 10 segundos, luego se moverá hacia la izquierda en el siguiente ciclo. Este movimiento continuo asegura que tu computadora no entre en estado de inactividad.

```sh
pip install pyautogui keyboard threading
