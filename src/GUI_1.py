import tkinter as tk

get_root_parameters=[0, 0, 0, 0, 0, 0, 0]
"""
0==> equation  1==> iterations  2==> epsilon
3==> xl        4==> xu          5==>xo
6==> g
"""


def period_parameter():
    for w in fr_param.winfo_children():
        w.destroy()
    tk.Label(fr_param, text="Parameters:").grid(row=0)
    tk.Label(fr_param, text="lower bound:").grid(row=1)
    tk.Label(fr_param, text="upper bound:").grid(row=2)

    get_root_parameters[3] = tk.Entry(fr_param).grid(row=1, column=1)
    get_root_parameters[4] = tk.Entry(fr_param).grid(row=2, column=1)


def xo_parameter():
    for w in fr_param.winfo_children():
        w.destroy()
    tk.Label(fr_param, text="Xo:").grid(row=1)
    get_root_parameters[5] = tk.Entry(fr_param).grid(row=1, column=1)


def secant_parameters():
    pass


master = tk.Tk()
master.title("Root finder ")

#  top frame
fr_top = tk.Frame(master, width=500)
fr_top.grid(row=0)
tk.Label(fr_top, text="Equation:").grid(row=0)
eq = tk.Entry(fr_top, borderwidth=3,border=5).grid(row=0, column=1, padx=10, pady=10)

tk.Label(fr_top, text="Technique:").grid(row=1)
techniques = {"1": "Bisection",
              "2": "False-position",
              "3": "Fixed point",
              "4": "Newton-Raphson",
              "5": "secant"}
used_technique = tk.StringVar(fr_top, "1")
for (val, text) in techniques.items():
    tk.Radiobutton(fr_top, text=text, variable=used_technique, value=val).grid()

#  parameter frame
fr_param = tk.Frame(master, bd=1, width=500)
fr_param.grid(row=1)
tk.Label(fr_param, text="Parameters:").grid(row=0)

if used_technique == "1" or used_technique == "2":
    period_parameter()
elif used_technique == "3" or used_technique == "4":
    xo_parameter()
elif used_technique == "5":
    secant_parameters()

#  bottom frame
fr_bottom = tk.Frame(master, bd=1, width=500)
fr_bottom.grid(row=2)
tk.Label(fr_bottom, text="Max number of Iterations:").grid(row=0)
tk.Label(fr_bottom, text="Epsilon:").grid(row=1)

iterations = tk.Entry(fr_bottom).grid(row=0, column=1)
epsilon = tk.Entry(fr_bottom).grid(row=1, column=1)



def get_root():
    tk.Label(master, text="now you will see secant power").grid()
    used_technique.set("3")


submit=tk.Button(master, text="Get Root", command=get_root).grid()


get_root_parameters[0] = str(eq.get())
get_root_parameters[1] = int(iterations.get())
get_root_parameters[2] = float(epsilon.get())

master.mainloop()
