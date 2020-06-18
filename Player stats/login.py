import csv
from tkinter import *
from functools import partial


def login():
    f=open("team.csv",'r+')
    csv_rec=csv.reader(f)
    for i in csv_rec:
        if i[0]==str(username.get()):
            if i[1]==str(password.get()):
                print("Logged in successfully")
                tkWindow.destroy()

                break
            else:
                print("incorrect password")
                break
                import login
           
                
    else:
        print("wrong Username or password")
        print("try again")
        tkWindow.destroy()
        import login
#window

tkWindow = Tk()  
tkWindow.geometry('200x100')  
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)



#login button
signupButton=Button(tkWindow,text="Login",command=login).grid(row=6,column=1)

tkWindow.mainloop()
