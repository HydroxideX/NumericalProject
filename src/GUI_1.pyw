from tkinter import *

get_root_parameters = ['' for _ in range(7)]
"""
0==> equation  1==> iterations  2==> epsilon
3==> xl        4==> xu          5==>xo
6==> g
"""


def period_parameter():
    for w in fr_param.winfo_children():
        w.destroy()
    Label(fr_param, text="Parameters:").grid(row=0)
    Label(fr_param, text="lower bound:").grid(row=1)
    Label(fr_param, text="upper bound:").grid(row=2)

    get_root_parameters[3] = Entry(fr_param).grid(row=1, column=1)
    get_root_parameters[4] = Entry(fr_param).grid(row=2, column=1)


def xo_parameter():
    for w in fr_param.winfo_children():
        w.destroy()
    Label(fr_param, text="Xo:").grid(row=1)
    get_root_parameters[5] = Entry(fr_param).grid(row=1, column=1)


def secant_parameters():
    pass


master = Tk()
master.title("Root finder ")

#  top frame
fr_top = Frame(master, width=500)
fr_top.grid(row=0)
Label(fr_top, text="Equation:").grid(row=0)
eq = Entry(fr_top, borderwidth=3, border=5).grid(row=0, column=1, padx=10, pady=10)

Label(fr_top, text="Technique:").grid(row=1)
techniques = {"1": "Bisection",
              "2": "False-position",
              "3": "Fixed point",
              "4": "Newton-Raphson",
              "5": "secant"}
used_technique = StringVar(fr_top, "1")
for (val, text) in techniques.items():
    Radiobutton(fr_top, text=text, variable=used_technique, value=val).grid()

#  parameter frame
fr_param = Frame(master, bd=1, width=500)
fr_param.grid(row=1)
Label(fr_param, text="Parameters:").grid(row=0)

if used_technique == "1" or used_technique == "2":
    period_parameter()
elif used_technique == "3" or used_technique == "4":
    xo_parameter()
elif used_technique == "5":
    secant_parameters()

#  bottom frame
fr_bottom = Frame(master, bd=1, width=500)
fr_bottom.grid(row=2)
Label(fr_bottom, text="Max number of Iterations:").grid(row=0)
Label(fr_bottom, text="Epsilon:").grid(row=1)

iterations = Entry(fr_bottom).grid(row=0, column=1)
epsilon = Entry(fr_bottom).grid(row=1, column=1)


def get_root():
    Label(master, text="now you will see secant power").grid()
    used_technique.set("3")


submit = Button(master, text="Get Root", command=get_root).grid()


def extract_input():
    get_root_parameters[0] = eq.get()
    get_root_parameters[1] = iterations.get()
    get_root_parameters[2] = epsilon.get()


master.mainloop()
