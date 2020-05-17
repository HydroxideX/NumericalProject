from tkinter import *

root = Tk()
root.title('Interpolation')
root.geometry('200x200')

var = IntVar()

Label(root, text='Points').pack(anchor=W)
L1 = Entry(root)
L1.pack(anchor=W)
R1 = Radiobutton(root, text="Newton", variable=var, value=1)
R1.pack(anchor=W)
R2 = Radiobutton(root, text="Lagrange", variable=var, value=2)
R2.pack(anchor=W)
B1 = Button(root, text='from file', width=10)
B1.pack(anchor=W)
B2 = Button(root, text='Solve', width=10)
B2.pack(anchor=W)


label = Label(root)
label.pack()
root.mainloop()
