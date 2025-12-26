import tkinter
t = Tk()

L1 = Label(text="Name")
L1.pack()
E1 = Entry()
E1.pack()

r1 = Radiobutton(text="Male")
r1.pack()
r2 = Radiobutton(text="Female")
r2.pack()

c = Checkbutton(text="I Agree To Share my Gender and Name to this Organisation")

b = Button(text="Submit")
b.pack()