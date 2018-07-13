import time, os
from pynput import keyboard, mouse
from threading import Thread
from pynput.mouse import Button, Controller
from Window import Wind
WAIT=0.04
toggle8,toggle9 = False, False
mouse1 = Controller()
def f():
    while True:
        if toggle9:
            mouse1.press(Button.left)
            time.sleep(WAIT)
            mouse1.release(Button.left)
        else:
            time.sleep(0.3)
        if toggle8:
            mouse1.press(Button.left)
        else:
            mouse1.release(Button.left)

def on_release(key):
    global toggle9, toggle8
    print(key)
    if str(key) == "'l'":
        toggle9 = False


def on_press(key):
    global toggle9, toggle8
    if str(key) == "Key.ctrl_r":
        os._exit(1)
    if str(key) == "'l'":
        toggle9 = True

#    else: print(key)
#    if str(key) == "'`'":
#       toggle = not toggle

def on_click(x, y, button, pressed):
    global toggle9,toggle8
    if str(button) == "Button.button20":
        if pressed:
            toggle9 = True
        else:
            toggle9 = False
    if str(button) == "Button.button8" and pressed:
        toggle8 = not toggle8




def f1():
    with keyboard.Listener(on_press=on_press, on_release = on_release) as listener:listener.join()
def f2():
    with mouse.Listener(on_click=on_click ) as listener:listener.join()
def f3():
    Wind()


th,th1,th2,th3= Thread(target=f),Thread(target=f1),Thread(target=f2),Thread(target=f3)



if __name__ == '__main__':
    th.start(),th1.start(),th2.start(),th3.start()
    th.join(),th1.join(),th2.join(),th3.join()


    '''
    def clickk(pres):
        T_O= 0
        T_T= 0
        if pres == True:
            while pres:
                print(WAIT, T_O, T_T)
                if (T_T+time.time())>(T_O+WAIT):
                    print(time.time()),
                    T_O = time.time(),
                    mouse1.press(Button.left),
                    mouse1.release(Button.left)
        else: return

    def on_click(x, y, button, pressed):
        if (str(button) == "Button.button9"): clickk(pressed)
    '''

