import tkinter as tk
from tkinter import *
import playsound

window = Tk()
window.attributes('-topmost',True)
window.title('sound baord')

idog = PhotoImage(file='dog.png')
bdog = Button(window, image=idog, width=180, height=180)
ibooing = PhotoImage(file='booing.png')
bbooing = Button(window, image=ibooing, width=180, height=180)
icheering = PhotoImage(file='cheering.png')
bcheering = Button(window, image=icheering, width=180, height=180)
ilaughing = PhotoImage(file='laughing.png')
blaughing = Button(window, image=ilaughing, width=180, height=180)
irain = PhotoImage(file='rain.png')
brain = Button(window, image=irain, width=180, height=180)

def dog(event):
    print(event)
    playsound.playsound('file.mp3', block=False)
def booing(event):
    print(event)
    playsound.playsound('booing.mp3', block=False)
def cheering(event):
    print(event)
    playsound.playsound('cheering.mp3', block=False)
def laughing(event):
    print(event)
    playsound.playsound('laughing.mp3', block=False)
def rain(event):
    print(event)
    playsound.playsound('rain.mp3', block=False)

bdog.bind('<Button>', dog)
bbooing.bind('<Button>', booing)
bcheering.bind('<Button>', cheering)
blaughing.bind('<Button>', laughing)
brain.bind('<Button>', rain)

bdog.grid(row= 1, column= 1, padx=2, pady=2)
bbooing.grid(row= 1, column= 2, padx=2, pady=2)
brain.grid(row=1, column=3, padx=2, pady=2)
bcheering.grid(row= 2, column= 1, padx=2, pady=2)
blaughing.grid(row= 2, column= 2, padx=2, pady=2)

window.mainloop()