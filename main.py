from customtkinter import *
from logic import Button_Press

root = CTk()
root.title("Python customtkinter Calculator")
root.geometry("645x750")

Entry = CTkEntry(root,
                 height=120,width=635,
                 justify = 'right',font=("Stencil Std",65))

frame_button = CTkFrame(root,
                        width=615,height=615,
                        bg_color='#555555')

Button_AC = CTkButton(frame_button,
                     text="AC",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(0,Entry))

Button_1 = CTkButton(frame_button,
                     text="1",
                     font=("Stencil Std",65),
                     command=lambda:Button_Press(1,Entry))

Entry.place(x=6,y=5)
frame_button.place(x=15,y=125)

Button_AC.pack()

root.mainloop()