from customtkinter import END

# Defining Function To Place The Number Associated With The Pressed Button Into EntryBox
def Button_Press(X,Ent):
    Ent.insert(END,X)

# Defining Function To Clear The Entry Box
def All_Clear(Ent):
    Ent.delete(0,END)

# Defining Function To Find THe Total
def Total(Ent):
    # Geting The Value Stored Within The EntryBox
    value = Ent.get()

    # Trying To Find The Total Without Any Errors
    try:
        if value == '':
            value = '0'

        # Solving The Question Equation
        total = float(eval(value))

        # Triming It Down To 6 Decimal Places
        total = "{:.6f}".format(total)

        total = str(total)

        # Removing '0' and '.' If Not any Or After Deciaml Places
        total = total.rstrip('0')
        if total[-1] == '.':
            total = total[:-1]

        # Displaying The Total In The EntryBox
        All_Clear(Ent)
        Ent.insert(END,total)

    # Dealing With Errors
    except(ValueError,RuntimeError,NameError,TypeError,IndexError,SyntaxError):
        All_Clear(Ent)
        Ent.insert(END,"An Error Has Occured Press The AC Key And Try Again")
        print("An Error Has Occured Pls Press The AC Key And Try Again \n"*15)

    # Dealing With Divide By Zero Error
    except(ZeroDivisionError):

        # Funny
        from webbrowser import open
        #from random import random

        open("https://www.youtube.com/watch?v=WI_qPBQhJSM")
        All_Clear(Ent)
        Button_Press("LMAO!!",Ent)
        #x = random()

        #if(x<0.26):
            #open('https://youtu.be/GDg9lWcdqDc?t=10')
        #elif(x>0.24 & x<0.51):
            #open('https://youtu.be/nlLhw1mtCFA')
        #elif(x>0.49 & x<0.76):
            #open("https://youtu.be/xPh-5P4XH6o?t=104")
        #elif(x>0.74):
            #open("https://youtu.be/srjLwgtcxYo")

        #if (x>0.2 and x<0.3):
            #open('https://youtu.be/GDg9lWcdqDc?t=10')
            #open('https://youtu.be/nlLhw1mtCFA')
            #open("https://youtu.be/xPh-5P4XH6o?t=104")
            #open("https://youtu.be/srjLwgtcxYo")
