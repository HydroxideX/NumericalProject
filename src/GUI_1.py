import tkinter as tk

# hi shbb

master = tk.Tk()
master.title("Root finder ")

#  top frame
fr_top = tk.Frame(master, width=500)
fr_top.pack()

tk.Label(fr_top, text="Equation :").grid(row=0)
eq = tk.Entry(fr_top)
eq.grid(row=0, column=1)

tk.Label(fr_top, text="Technique :").grid(row=1)
v = tk.StringVar(fr_top, "1")
techniques_values = {"Bisection": "1",
                     "False-position": "2",
                     "Fixed point": "3",
                     "Newton-Raphson": "4",
                     "secant": "5"}

for (text, value) in techniques_values.items():
    tk.Radiobutton(fr_top, text=text, variable=v, value=value).grid()

#  parameter frame
fr_param = tk.Frame(master, bd=1, width=500)
fr_param.pack()
tk.Label(fr_param).grid(row=0)

#  bottom frame
fr_bottom = tk.Frame(master, bd=1, width=500)
fr_bottom.pack()

tk.Label(fr_bottom, text="Max number of Iterations:").grid(row=0)
tk.Label(fr_bottom, text="Epsilon:").grid(row=1)

iterations = tk.Entry(fr_bottom)
Epsilon = tk.Entry(fr_bottom)
iterations.grid(row=0, column=1)
Epsilon.grid(row=1, column=1)

master.mainloop()
