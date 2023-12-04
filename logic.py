from customtkinter import *
from math import *

def Button_Press(X,Ent):
    Ent.insert(END,X)

def All_Clear(Ent):
    Ent.delete(0,END)

def Total(Ent):
    value = Ent.get()

    if value == '':
        value = '0'

    total = float(eval(value))

    total = "{:.6f}".format(total)

    total = str(total)

    total = total.rstrip('0')
    if total[-1] == '.':
        total = total[:-1]

    All_Clear(Ent)
    Ent.insert(END,total)

