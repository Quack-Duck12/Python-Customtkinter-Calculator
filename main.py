from customtkinter import *
from logic import Button_Press,All_Clear,Total

root = CTk()
root.title("Python customtkinter Calculator")
root.geometry("709x791")

Entry = CTkEntry(root,
                 height=144,width=692,
                 justify = 'right',font=("Stencil Std",65))

class Buttons:

    def __init__(self,var):

        self.Test_Button = CTkButton(root,
                     text=str(var),
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(var,Entry),
                     width=170,height=120,
                     corner_radius=20)
        
    def place(self,x,y):
        self.Test_Button.place(x=x, y=y)


Button_Div = Buttons("/")
Button_Mult = Buttons("*")
Button_Minus = Buttons("-")
Button_Plus = Buttons("+")
Button_Dot = Buttons(".")
Button_Bracket_Open = Buttons("(")
Button_Bracket_Close = Buttons(")")

Button_7 = Buttons(7)
Button_8 = Buttons(8)
Button_9 = Buttons(9)

Button_4 = Buttons(4)
Button_5 = Buttons(5)
Button_6 = Buttons(6)

Button_1 = Buttons(1)
Button_2 = Buttons(2)
Button_3 =Buttons(3)



Button_AC = CTkButton(root,
                     text="AC",
                     font=("Stencil Std",65),
                     command=lambda:All_Clear(Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_Equals = CTkButton(root,
                     text="=",
                     font=("Stencil Std",65),
                     command=lambda:Total(Entry),
                     width=170,height=120,
                     corner_radius=20)

Entry.place(x=10,y=10)

Button_AC.place(x=7,y=164)
Button_Div.place(x=182,y=164)
Button_Mult.place(x=357,y=164)
Button_Minus.place(x=532,y=164)

Button_7.place(x=7,y=289)
Button_8.place(x=182,y=289)
Button_9.place(x=357,y=289)
Button_Plus.place(x=532,y=289)

Button_4.place(x=7,y=414)
Button_5.place(x=182,y=414)
Button_6.place(x=357,y=414)
Button_Bracket_Open.place(x=532,y=414)

Button_1.place(x=7,y=539)

Button_Equals.place(x=200,y=400)

root.mainloop()