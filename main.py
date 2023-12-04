from customtkinter import *
from logic import Button_Press,All_Clear,Total

root = CTk()
root.title("Python customtkinter Calculator")
root.geometry("709x791")

Entry = CTkEntry(root,
                 height=144,width=692,
                 justify = 'right',font=("Stencil Std",65))

Button_AC = CTkButton(root,
                     text="AC",
                     font=("Stencil Std",65),
                     command=lambda:All_Clear(Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_Div = CTkButton(root,
                     text="/",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press('/',Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_Mult = CTkButton(root,
                     text="*",
                     font=("Stencil Std",100),
                     command=lambda:Button_Press('*',Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_Minus = CTkButton(root,
                     text="-",
                     font=("Stencil Std",100),
                     command=lambda:Button_Press("-",Entry),
                     width=170,height=120,
                     corner_radius=20)



Button_7 = CTkButton(root,
                     text="7",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(7,Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_8 = CTkButton(root,
                     text="8",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(8,Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_9 = CTkButton(root,
                     text="9",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(9,Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_Plus = CTkButton(root,
                     text="+",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press("+",Entry),
                     width=170,height=120,
                     corner_radius=20)



Button_4 = CTkButton(root,
                     text="4",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(4,Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_5 = CTkButton(root,
                     text="5",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(5,Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_6 = CTkButton(root,
                     text="6",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(6,Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_Bracket_Open = CTkButton(root,
                     text="(",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press("(",Entry),
                     width=170,height=120,
                     corner_radius=20)



Button_1 = CTkButton(root,
                     text="1",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(1,Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_2 = CTkButton(root,
                     text="2",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(2,Entry),
                     width=170,height=120,
                     corner_radius=20)

Button_3 = CTkButton(root,
                     text="3",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(3,Entry),
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

#Button_Equals.place(x=200,y=400)

root.mainloop()