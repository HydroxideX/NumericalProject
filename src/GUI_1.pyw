import BisectionMethod
import FalsePosition
import FixedPoint
import NewtonRaphson
import Secant
import Plot
from tkinter import *


def extract_input():
    if not(used_technique.get() == "3" or used_technique.get() == "4"):
        s=float(X2.get())
    else:
        if used_technique.get() == "3":
            s = str(X2.get())
        else:
            s=0
    f = float(X1.get())
    eps =epsilon.get()
    if eps == "":
        eps = None
    else:
        eps = float(eps)

    iter_num = iterations.get()
    if iter_num == "":
        iter_num = None
    else:
        iter_num = int(iter_num)

    get_root(used_technique.get(), eq.get(), iter_num, eps, f, s)


def get_root(technique,get_root_equation,get_root_iterations,get_root_epsilon,get_root_x1 ,get_root_x2 = 0):
    if technique == "1":
        print(BisectionMethod.bisection(get_root_x1, get_root_x2, get_root_equation, get_root_epsilon, get_root_iterations))
    elif technique == "2":
        print(FalsePosition.false_position(get_root_x1, get_root_x2, get_root_equation, get_root_epsilon, get_root_iterations))
    elif technique == "3":
        print(FixedPoint.fixed_point(get_root_x1, get_root_epsilon, get_root_iterations, get_root_x2))
    elif technique == "4":
        print(NewtonRaphson.newton_raphson(get_root_x1, get_root_epsilon, get_root_iterations, get_root_equation))
    elif technique == "5":
        print(Secant.secant(get_root_x1, get_root_x2, get_root_iterations, get_root_epsilon, get_root_equation))


def parameters():
    for w in fr_param.winfo_children():
        w.destroy()
    t = used_technique.get()
    l5 = Label(fr_param, text="Parameters:")
    x1 = StringVar()
    x2 = StringVar()

    if t == "4" or t == "3":
        x1.set("Xo")
        if t == "3":
            x2.set("g(x)")

    else:
        if t == "1" or t == "2" :
            x1.set("Xl")
            x2.set("Xu")
        else:
            x1.set("X1")
            x2.set("X2")
    l6 = Label(fr_param, textvariable=x1)
    l5.grid(row=0)
    l6.grid(row=1)
    first_x = Entry(fr_param,textvariable=X1, borderwidth=3, border=5)
    first_x.grid(row=1, column=1, padx=10, pady=10)
    if t != "4":
        l7 = Label(fr_param, textvariable=x2)
        second_x = Entry(fr_param, textvariable=X2, borderwidth=3, border=5)
        l7.grid(row=2)
        second_x.grid(row=2, column=1, padx=10, pady=10)


# GUI
master = Tk()
master.title("Root finder ")

#  top frame
fr_top = Frame(master, width=500)
l1=Label(fr_top, text="Equation:")
eq = Entry(fr_top, borderwidth=3, border=5)
l2=Label(fr_top, text="Max number of Iterations:")
l3=Label(fr_top, text="Epsilon:")
iterations = Entry(fr_top, borderwidth=3, border=5)
epsilon = Entry(fr_top, borderwidth=3, border=5)

iterations.grid(row=1, column=1, padx=10, pady=10)
epsilon.grid(row=2, column=1, padx=10, pady=10)
l4=Label(fr_top, text="Technique:")
techniques = {"1": "Bisection",
              "2": "False-position",
              "3": "Fixed point",
              "4": "Newton-Raphson",
              "5": "secant"}
used_technique = StringVar(fr_top, "1")
X1 = StringVar()
X2 = StringVar()
for (val, text) in techniques.items():
    Radiobutton(fr_top, text=text, variable=used_technique, value=val,command=parameters).grid(column=1, sticky=W)

#  parameter frame
fr_param = Frame(master, bd=1, width=500)

submit = Button(master, text="Get Root", command=extract_input)

fr_top.grid(row=0)
l1.grid(row=0)
eq.grid(row=0, column=1, padx=10, pady=10)
l2.grid(row=1)
l3.grid(row=2)
l4.grid(row=3)
fr_param.grid(row=1)
submit.grid(row=2)
master.mainloop()
