import pyautogui
import time

# Función para abrir Paint
def open_paint():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('paint')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)  # Esperar a que Paint se abra completamente

# Llamar a la función para abrir Paint
open_paint()

# Asegúrate de que Paint esté maximizado y listo para dibujar
pyautogui.hotkey('win', 'up')  # Maximizar la ventana actual
time.sleep(1)

# Mover el mouse a la posición inicial
pyautogui.moveTo(400, 300)

# Dibujar una espiral
distance = 200
change = 20

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)   # Mover derecha
    distance -= change
    pyautogui.dragRel(0, distance, duration=0.2)   # Mover abajo
    pyautogui.dragRel(-distance, 0, duration=0.2)  # Mover izquierda
    distance -= change
    pyautogui.dragRel(0, -distance, duration=0.2)  # Mover arriba

# Guardar el archivo
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('espiral.png')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')  # Confirmar guardar si aparece una advertencia de formato

print("Dibujo completado y guardado como espiral.png")
