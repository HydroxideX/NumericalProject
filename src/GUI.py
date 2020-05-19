from tkinter import *

import NewtonInterpolation
import lagrangeInterpolation
import PolynomialPlot

root = Tk()
root.title('Interpolation')
root.geometry('300x340')

var = IntVar()

L4 = Label(root, text='Result')
L5 = Label(root, text='Time')
L6 = Label(root, text='Polynomial')
L1 = Label(root, text='Points')
T1 = Entry(root)
L2 = Label(root, text='Value')
T2 = Entry(root)
L3 = Label(root, text='Order')
T3 = Entry(root)
order = T3.get()
R1 = Radiobutton(root, text="Newton", variable=var, value=0)
R2 = Radiobutton(root, text="Lagrange", variable=var, value=1)


def solve():
    x = int(T2.get())
    values = T1.get()
    values = values.split(' ')
    points = []
    for i in range(0, len(values), 2):
        points.append((int(values[i]), int(values[i + 1])))
    if var.get() == 0:
        answer = NewtonInterpolation.interpolate(points, x)
        L4.configure(text=answer[0])
        L5.configure(text=answer[2])
        L6.configure(text=answer[1])
    else:
        answer = lagrangeInterpolation.interpolate(points, x)
        L4.configure(text=answer[0])
        L5.configure(text=answer[1])
        L6.configure(text="Polynomial")

def plot():
    values = T1.get()
    values = values.split(' ')
    points = []
    for i in range(0, len(values), 2):
        points.append((int(values[i]), int(values[i + 1])))
    PolynomialPlot.plot(points)


B1 = Button(root, text='from file', width=10)
B2 = Button(root, text='Plot', width=10, command=plot)
B3 = Button(root, text='Solve', width=10, command=solve)

L1.pack()
T1.pack()
L2.pack()
T2.pack()
L3.pack()
T3.pack()
R1.pack()
R2.pack()
B1.pack()
B2.pack()
B3.pack()
L4.pack()
L5.pack()
L6.pack()

root.mainloop()
