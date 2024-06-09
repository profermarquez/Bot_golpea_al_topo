# https://www.classicgame.com/game/Whack+a+Mole
# imports
import cv2
import pyautogui
from time import sleep

# Esto significa que pyautogui no esperará nada entre
# las acciones, lo que hace que las operaciones se ejecuten 
# lo más rápido posible.
pyautogui.PAUSE = 0

# template and dimensions
template = cv2.imread("imgs/nose.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
template_w, template_h = template_gray.shape[::-1]

# dimensiones de la ventana del juego
x, y, w, h = 523, 247, 875, 679

# Espera
sleep(3)

# Prgrama principal
while True:

    # Realiza la captura de pantalla
    pyautogui.screenshot("imgs/image.png", region=(x, y, w, h))
    image = cv2.imread("imgs/image.png")

    # muesta lo que la computadora ve
    image_mini = cv2.resize(
        src=image,
        dsize=(800, 600)  # debe ser entera
    )
    cv2.imshow("vision", image_mini)
    if cv2.waitKey(10) & 0xFF == 27:  # Si presiona Esc sale
        break

    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Codigo que compara la imagen con la captura
    result = cv2.matchTemplate(
        image=image_gray,
        templ=template_gray,
        method=cv2.TM_CCOEFF_NORMED
    )

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print(max_val >= 0.5)
    
    # si la igualdad de la comparacón es mayo a 0.5 entonces hago click
    if max_val >= 0.5:
        pyautogui.click(
            x=max_loc[0] + x,  # screen x
            y=max_loc[1] + y  # screen y
        )

        image = cv2.rectangle(
            img=image,
            pt1=max_loc,
            pt2=(
                max_loc[0] + template_w,  # = pt2 x
                max_loc[1] + template_h  # = pt2 y
            ),
            color=(0, 0, 255), # El color del rectángulo
            thickness=-1  # El grosor del rectángulo
        )
        #print("Click")

    # espera un poco antes de la siguiente iteración
    sleep(0.1)
