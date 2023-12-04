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

        # Getting User IP Address
        from socket import gethostbyname,gethostname

        hostname = gethostname()
        ip_address = gethostbyname(hostname)

        # Funny https://youtu.be/C7EocA1hsCU?si=oJ1f8mF910gaFI9C 
        All_Clear(Ent)
        Ent.insert(END,f"Your Ip: {ip_address}")
        print("https://youtu.be/GDg9lWcdqDc?t=10\n"*25)
