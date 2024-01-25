import tkinter as tk
from tkinter import *
import playsound, time

window = Tk()
window.attributes('-topmost',True)
window.title('test')

lanum = ('4','6','7','8','23','3','98','54','x^2','(4x + 3)')
laop = ('+','-','-','+','*','*','/','*','+','')
lbnum = ('9','3','76','5','2','7','3','65','1','(x - 2)')
lbop = ('','','+','+','','*','','/','-','')
lthenum = ('','','9','20','','12','','6','12','')
lbuton = ('=','=','=','=','=','=','=','=','Factor','FIOL')
anser = ('13','3','-49','33','46','252','32.67','585','(x + 4)(x - 3)','4x^2 - 5x - 6')
i = 0

anum = tk.StringVar()
anum.set('4')
aop = tk.StringVar()
aop.set('+')
bnum = tk.StringVar()
bnum.set('9')
bop = tk.StringVar()
bop.set('')
thenum = tk.StringVar()
thenum.set('')
buton = tk.StringVar()
buton.set('=')

num1 = Label(window, textvariable=anum)
op1 = Label(window, textvariable=aop)
num2 = Label(window, textvariable=bnum)
op2 = Label(window, textvariable=bop)
num3 = Label(window, textvariable=thenum)
equ = Label(window, textvariable=buton)
e = Entry(window)
b = Button(window, text='Check')

def go(event):
    global i
    print(event)
    if e.get() == anser[i] and i != 9:
        i = i + 1
        anum.set(lanum[i])
        aop.set(laop[i])
        bnum.set(lbnum[i])
        bop.set(lbop[i])
        thenum.set(lthenum[i])
        buton.set(lbuton[i])
        e.delete(0,END)
        playsound.playsound('cheering.mp3', block=False)
    elif  e.get() == anser[i] and i == 9:
        i = i + 1
        playsound.playsound('cheering.mp3', block=False)
        time.sleep(0.2)
        playsound.playsound('laughing.mp3', block=False)
        time.sleep(0.2)
        playsound.playsound('cheering.mp3', block=False)
        anum.set('')
        aop.set('')
        bnum.set('You Win!!!')
        bop.set('')
        thenum.set('')
        buton.set('')
        e.delete(0,END)
    elif i != 10:
        playsound.playsound('booing.mp3', block=False)
    else:
        playsound.playsound('cheering.mp3', block=False)
        time.sleep(0.2)
        playsound.playsound('laughing.mp3', block=False)
        time.sleep(0.2)
        playsound.playsound('cheering.mp3', block=False)

b.bind('<Button>', go)

num1.grid(row=1, column=1)
op1.grid(row=1, column=2)
num2.grid(row=1, column=3)
op2.grid(row=1, column=4)
num3.grid(row=1, column=5)
equ.grid(row=1, column=6)
e.grid(row=1, column=7)
b.grid(row=2, column=1, columnspan=7)

window.mainloop()