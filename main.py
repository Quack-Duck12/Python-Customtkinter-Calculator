from customtkinter import *
from logic import Button_Press,All_Clear

root = CTk()
root.title("Python customtkinter Calculator")
root.geometry("709x791")

Entry = CTkEntry(root,
                 height=120,width=635,
                 justify = 'right',font=("Stencil Std",65))



Button_AC = CTkButton(root,
                     text="AC",
                     font=("Stencil Std",65),
                     command=lambda:All_Clear(Entry),
                     width=170,height=120)

Button_Div = CTkButton(root,
                     text="/",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press('/',Entry),
                     width=170,height=120)

Button_Mult = CTkButton(root,
                     text="*",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press('*',Entry),
                     width=170,height=120)

Button_Minus = CTkButton(root,
                     text="-",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press("-",Entry),
                     width=170,height=120)



Button_7 = CTkButton(root,
                     text="7",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(7,Entry),
                     width=170,height=120)

Button_8 = CTkButton(root,
                     text="8",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(8,Entry),
                     width=170,height=120)

Button_9 = CTkButton(root,
                     text="9",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(9,Entry),
                     width=170,height=120)


Button_4 = CTkButton(root,
                     text="4",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(4,Entry),
                     width=170,height=120)

Button_5 = CTkButton(root,
                     text="5",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(5,Entry),
                     width=170,height=120)

Button_6 = CTkButton(root,
                     text="6",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(6,Entry),
                     width=170,height=120)

Entry.place(x=6,y=5)

Button_AC.place(x=5,y=130)
Button_Div.pack()
Button_Mult.pack()
Button_Minus.pack()

Button_7.pack()
Button_8.pack()
Button_9.pack()

Button_4.pack()
Button_5.pack()
Button_6.pack()

root.mainloop()