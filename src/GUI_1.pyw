import BisectionMethod
import FalsePosition
import FixedPoint
import NewtonRaphson
import Secant
from tkinter import *

get_root_equation="x"
get_root_iterations=50
get_root_epsilon=0.0001
get_root_xu=1
get_root_xl=0
get_root_xo=0
get_root_g="x"
get_root_x1=0
get_root_x2=1


def extract_input():
    global get_root_equation
    get_root_equation = eq.get()
    global get_root_iterations
    get_root_iterations = iterations.get()
    global get_root_epsilon
    get_root_epsilon = epsilon.get()


def period_parameter():
    for w in fr_param.winfo_children():
        w.destroy()
    Label(fr_param, text="Parameters:").grid(row=0)
    Label(fr_param, text="Xl=").grid(row=1)
    Label(fr_param, text="Xu=").grid(row=2)

    xl = Entry(fr_param, borderwidth=3, border=5).grid(row=1, column=1, padx=10, pady=10)
    xu = Entry(fr_param, borderwidth=3, border=5).grid(row=2, column=1, padx=10, pady=10)
    global get_root_xl
    get_root_xl = xl.get()
    global get_root_xu
    get_root_xu = xu.get()



def xo_parameter():
    for w in fr_param.winfo_children():
        w.destroy()
    Label(fr_param, text="Parameters:").grid(row=0)
    Label(fr_param, text="Xo=").grid(row=1)
    xo = Entry(fr_param, borderwidth=3, border=5).grid(row=1, column=1, padx=10, pady=10)
    global get_root_xo
    get_root_xo = xo.get()


def x1_x2_parameter():
    for w in fr_param.winfo_children():
        w.destroy()
    Label(fr_param, text="Parameters:").grid(row=0)
    Label(fr_param, text="X1=").grid(row=1)
    Label(fr_param, text="X2=").grid(row=2)

    x1 = Entry(fr_param, borderwidth=3, border=5).grid(row=1, column=1, padx=10, pady=10)
    x2 = Entry(fr_param, borderwidth=3, border=5).grid(row=2, column=1, padx=10, pady=10)
    global get_root_x1
    get_root_x1 = x1.get()
    global get_root_x2
    get_root_x2 = x2.get()


def print_parameters(value):
    if value == "1" or value == "2":
        period_parameter()
    elif value == "3" or value == "4":
        xo_parameter()
    elif value == "5":
        x1_x2_parameter()


def get_root(technique):
    if technique == "1":
        print(BisectionMethod.bisection(get_root_xl, get_root_xu, get_root_equation, get_root_epsilon, get_root_iterations))
    elif technique == "2":
        print(FalsePosition.false_position(get_root_xl, get_root_xu, get_root_equation, get_root_epsilon, get_root_iterations))
    elif technique == "3":
        print(FixedPoint.fixed_point(get_root_xo, get_root_epsilon, get_root_iterations, get_root_g))
    elif technique == "4":
        print(NewtonRaphson.newton_raphson(get_root_xo, get_root_epsilon, get_root_iterations, get_root_equation))
    elif technique == "5":
        print(Secant.secant(get_root_x1, get_root_x2, get_root_iterations, get_root_epsilon, get_root_equation))


master = Tk()
master.title("Root finder ")

#  top frame
fr_top = Frame(master, width=500)
fr_top.grid(row=0)
Label(fr_top, text="Equation:").grid(row=0)
eq = Entry(fr_top, borderwidth=3, border=5).grid(row=0, column=1, padx=10, pady=10)

Label(fr_top, text="Max number of Iterations:").grid(row=1)
Label(fr_top, text="Epsilon:").grid(row=2)

iterations = Entry(fr_top, borderwidth=3, border=5).grid(row=1, column=1, padx=10, pady=10)
epsilon = Entry(fr_top, borderwidth=3, border=5).grid(row=2, column=1, padx=10, pady=10)

Label(fr_top, text="Technique:").grid(row=3)
techniques = {"1": "Bisection",
              "2": "False-position",
              "3": "Fixed point",
              "4": "Newton-Raphson",
              "5": "secant"}
used_technique = StringVar(master, "1")

for (val, text) in techniques.items():
    Radiobutton(fr_top, text=text, variable=used_technique, value=val, command=lambda: print_parameters(used_technique.get())).grid(column=1,sticky=W)

#  parameter frame
fr_param = Frame(master, bd=1, width=500)
fr_param.grid(row=1)


submit=Button(master, text="Get Root", command=lambda: get_root(used_technique.get())).grid()

master.mainloop()
