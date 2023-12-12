# Importing Necessary Modules
from customtkinter import *
from logic import *

# Initilizing The Window
root = CTk()
root.title("Python customtkinter Calculator")
root.geometry("709x791")
root.resizable(False,False)

# Creating EntryBox To Work With
Entry = CTkEntry(root,
                 height=144,width=692,
                 justify = 'right',font=("Stencil Std",65))

# Defining Buttons Class To Make Button Declaring Work Easier
class Buttons:

    def __init__(self,var):

        # Creating Button Class
        self.Test_Button = CTkButton(root,
                     text=str(var),
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(var,Entry),
                     width=170,height=120,
                     corner_radius=20,
                     fg_color="#164882",
                     hover_color="#132540")

    # Defining Function place To Place The Buttons Declared Using Class Easier To Place
    def place(self,x,y):
        self.Test_Button.place(x=x, y=y)

# Declaring Most Of The Button Using Class Buttons
Button_Div = Buttons("/")
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
Button_3 = Buttons(3)

Button_0 = Buttons(0)


# Declaring Buttons With Seprate Apperance Or Functions
Button_AC = CTkButton(root,
                     text="AC",
                     font=("Stencil Std",65),
                     command=lambda:All_Clear(Entry),
                     width=170,height=120,
                     corner_radius=20,
                     fg_color="#164882",
                     hover_color="#132540")

Button_BackSpace = CTkButton(root,
                     font=("Stencil Std",26),
                     command=lambda:BackSpace(Entry),
                     width=170,height=120,
                     corner_radius=20,
                     fg_color="#164882",
                     hover_color="#132540",
                     text="BackSpace",)

Button_Equals = CTkButton(root,
                     text="=",
                     font=("Stencil Std",65),
                     command=lambda:Total(Entry),
                     width=170,height=120,
                     corner_radius=20,
                     fg_color="#164882",
                     hover_color="#132540")

Button_Mult = CTkButton(root,
                     text="*",
                     font=("Stencil Std",80),
                     command=lambda:Button_Press('*',Entry),
                     width=170,height=120,
                     corner_radius=20,
                     fg_color="#164882",
                     hover_color="#132540")

# Placing The Buttons And EntryBox
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
Button_2.place(x=182,y=539)
Button_3.place(x=357,y=539)
Button_Bracket_Close.place(x=532,y=539)

Button_0.place(x=7,y=664)
Button_Dot.place(x=182,y=664)
Button_BackSpace.place(x=357,y=664)
Button_Equals.place(x=532,y=664)

# Mainloop
root.mainloop()
