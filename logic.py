from customtkinter import *

def Button_Press(X,Ent):
    Ent.insert(END,X)

def All_Clear(Ent):
    Ent.delete(0,END)

def Total(Ent):
    value = Ent.get()

    try:
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

    except(ValueError,RuntimeError,NameError,TypeError,IndexError,SyntaxError):
        All_Clear(Ent)
        Ent.insert(END,"An Error Has Occured Press The AC Key And Try Again")
        print("An Error Has Occured Pls Press The AC Key And Try Again \n"*15)

    except(ZeroDivisionError):

        from socket import gethostbyname,gethostname

        hostname = gethostname()
        ip_address = gethostbyname(hostname)

        All_Clear(Ent)
        Ent.insert(END,f"Your Ip: {ip_address}")
        print("Dont Even Try \n"*15)
