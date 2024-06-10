import pyautogui
import time
import keyboard
import threading

print("########### NO TE QUEDES AFK :) ###########")
print("\n")
move = 500
pyautogui.FAILSAFE = False

# Crear un evento que usaremos para detener la función
stop_event = threading.Event()

# Crear un evento que usaremos para pausar y reanudar la función
pause_event = threading.Event()
pause_event.set()  # Inicialmente no está en pausa
def mover_mouse():
    direction = False
    itera = 1
    while not stop_event.is_set():
        print("### Presiona 'q' para detener ###")
        print("### Presiona 'p' para pausar/reanudar ###")
        # Esperar 10 segundos, pero permitir la interrupción para pausar
        elapsed_time = 0
        while elapsed_time < 10:
            start_time = time.time()
            if stop_event.is_set():
                return
            pause_event.wait()  # Espera hasta que se reanude si está en pausa
            if stop_event.is_set():
                return
            time.sleep(1)
            elapsed_time += time.time() - start_time
        
        if stop_event.is_set():
            return
        
        cord_x, cord_y = pyautogui.position()
        if direction:
            pyautogui.moveTo(cord_x+move)
            pyautogui.press('space')
            direction = False
        else:
            pyautogui.moveTo(cord_x-move)
            direction = True
        print('Movimiento... '+ str(itera))
        itera+=1
        print("\n")

# Ejecutar la función en un hilo separado
thread = threading.Thread(target=mover_mouse)
thread.start()

# Función para monitorear la pulsación de teclas
def esperar_tecla(): 
    while not stop_event.is_set():
        if keyboard.is_pressed('q'):
            stop_event.set()  # Establece el evento de parada cuando se presiona 'q'
            break
        if keyboard.is_pressed('p'):
            if pause_event.is_set():
                pause_event.clear()  # Pausa el movimiento
                print("########### Programa en pausa ###########")
            else:
                pause_event.set()  # Reanuda el movimiento
                print("########### Programa reanudado ###########")
            time.sleep(0.5)  # Espera un momento para evitar múltiples detecciones

# Crear un hilo separado para la espera de la tecla
tecla_thread = threading.Thread(target=esperar_tecla)
tecla_thread.start()

# Esperar a que el hilo termine
thread.join()
print("########### ADIOOOOOS :) ###########")
print("\n")
