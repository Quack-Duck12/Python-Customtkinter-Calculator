from customtkinter import *
from math import *

def Button_Press(X,Ent):
    Ent.insert(END,X)

def All_Clear(Ent):
    Ent.delete(0,END)

def Total(Ent):
    value = Ent.get()
    total = float(eval(value))
    All_Clear(Ent)
    Ent.insert(END,total)