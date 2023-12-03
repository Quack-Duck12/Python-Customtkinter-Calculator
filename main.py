from customtkinter import *

root = CTk()
root.title("Python customtkinter Calculator")
root.geometry("645x750")

Entry = CTkEntry(root,
                 height=120,width=635,
                 justify = 'right',font=("Stencil Std",65))

frame_button = CTkFrame(root,
                        width=615,height=615,
                        bg_color='#555555')

Entry.place(x=6,y=5)
frame_button.place(x=15,y=125)

root.mainloop()