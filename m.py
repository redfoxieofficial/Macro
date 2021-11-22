import time
from pynput import keyboard
from pynput.keyboard import Controller
from pynput import mouse

print("Mouse or Keyboard?")
print("***")
print("1 for Mouse")
print("2 for Keyboard")
choice = input("Choose: ")
saniye = input("How many clicks on second?: ")
saniye = float(saniye)
while choice == "1" or "2":
    if choice == "1":
        mouse = Controller()
        print('The current pointer position is {0}'.format(mouse.position))
        question = input("Do you want to set a mouse position (Y/N): ")
        if question.upper() == "Y":
            x = input("X: ")
            y = input("Y: ")
            mouse.position = (x, y)

        elif question.upper() == "N":
            pass
        else:
            print("Invalid Choice")
        print("Right Button Or Left Button: ")
        lr = input("L/R: ")
        if lr.upper() == "L":
            while True:
                mouse.press(mouse.Button.left)
                mouse.release(mouse.Button.left)
                time.sleep(float(saniye))
        elif lr.upper() == "R":
            while True:
                mouse.press(mouse.Button.Right)
                mouse.release(mouse.Button.Right)
                time.sleep(float(saniye))
        else:
            print("Invalid Choice")
    if choice == "2":
        tus = input("Which key do you want to press?: ")
        keyboard = Controller()
        while True:
            keyboard.press(tus)
            keyboard.release(tus)
            time.sleep(float(saniye))
    else:
        print("Invalid Choice")
