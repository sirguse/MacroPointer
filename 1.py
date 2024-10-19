import tkinter as tk
import pyautogui
import keyboard

def kursor(label):
    x,y = pyautogui.position()
    position = 'x: ' + str(x) + " y " + str(y)
    label.config(text=position)
    
    if keyboard.is_pressed('x'):
        root.destroy()
    else:
        label.after(5, kursor, label)  # Ponownie planuje wywołanie po 100 ms

root = tk.Tk()
root.title('Pozycja')
root.geometry('200x200')
label = tk.Label(root, font=('Arial', 16))
label.pack(pady=70)
tekst = tk.Label(root, text='W celu zamknięcia wciśnij "x".')
tekst.pack()

kursor(label)

root.mainloop()





"""""
import pyautogui
import keyboard
import tkinter as tk

def kursor(label):
    while True:
        x, y = pyautogui.position()
        position = "x: " + str(x) + ' y ' + str(y) 
        print(position)
        if keyboard.is_pressed('x'):
            break


 
root = tk.Tk()
root.title("Czytnik kursora")

root.geometry("200x200")
label = tk.Label(root)
kursor(label)

root.mainloop
"""