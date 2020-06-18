import csv
from tkinter import *
from functools import partial
def exit1():
    tkWindow1.destroy()
def clicked():
    list1=[]
    list2=[]
    with open("team.csv",'r+') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        for i in reader:
            list1.append(i)
    for i in range(len(list1)):
        if username.get()==list1[i][0]:
            print("Username taken")
            tkWindow1=Tk()
            tkWindow1.geometry('50x50')  
            tkWindow1.title('Try again')
            label1=Label(tkWindow1,text="TRY AGAIN\n Username taken").grid(row=0, column=0)
            
            tkWindow.destroy()
            import signup
            return
        else:
            continue
    list2.append(username.get())
    list2.append(password.get())
    list2.append(jersey.get())
    list2.append(team.get())
    
    print(list2)
    for i in range(5):
        list2.append(0)
    list1.append(list2)
    with open("team.csv",'w',newline='') as csv_file:
        csv_rec=csv.writer(csv_file)
        csv_rec.writerows(list1)
        print("Login created")
        tkWindow.destroy()
tkWindow = Tk()  
tkWindow.geometry('450x160')  
tkWindow.title('Signup')
tkWindow.configure(bg="black")

#username label and text entry box
usernameLabel = Label(tkWindow, text="\tUser Name\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=0, column=2)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=5)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="\tPassword\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=1, column=2)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=5)
Jerseylabel = Label(tkWindow, text="\tJersey number\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=4, column=2)
jersey = StringVar()
JerseyEntry = Entry(tkWindow, textvariable=jersey).grid(row=4, column=5)
Teamlabel=Label(tkWindow, text="\tTeam name\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=5, column=2)
team=StringVar()
TeamEntry=Entry(tkWindow,textvariable=team).grid(row=5, column=5)


#login button
signupButton = Button(tkWindow, text="Signup",fg="red",bg="black",font="Consolas 14 bold ",command=clicked).grid(row=10, column=4)


tkWindow.mainloop()

