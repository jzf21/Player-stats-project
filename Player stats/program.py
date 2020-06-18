from tkinter import*
from PIL import ImageTk, Image
def clicked():
    import login.py
def signup():
    import signup.py
window=Tk()
window.configure(bg='black')
window.title("WELCOME")

logo=ImageTk.PhotoImage(Image.open("rose.jpg"))
img1 = ImageTk.PhotoImage(Image.open("signup.gif"))
img = ImageTk.PhotoImage(Image.open("login.gif"))

explanation = """PLAYER STATS."""
word="""Signup HERE CLICK HERE"""

w = Label(window, compound = CENTER,text=explanation,fg="white",bg="black",font = "Helvetica 18 bold italic",image=logo).pack(side="left")
x = Label(window, compound = CENTER,text="""\n \n NEW MEMBER? \n SIGNUP   """,fg="red2",bg="black",font = "Helvetica 10 bold italic").pack(side="top")
loginButton = Button(window,bg="red",image=img,command=clicked).pack(side="top")
x = Label(window, compound = CENTER,text="""\n \n EXISTING USER? \n LOGIN    """,fg="red2",bg="black",font = "Helvetica 10 bold italic").pack(side="top")
signupButton=Button(window,bg="red2",image=img1,command=signup).pack(side="top")

window.mainloop()

