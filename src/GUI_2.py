import warnings
from tkinter import *
from tkinter.filedialog import askopenfile

import NewtonInterpolation
import lagrangeInterpolation
import PolynomialPlot

root = Tk()
root.title('Interpolation')
root.geometry('300x340')

var = IntVar()

L1 = Label(root, text='Points')
T1 = Entry(root)
L2 = Label(root, text='Value')
T2 = Entry(root)
L3 = Label(root, text='Order')
T3 = Entry(root)
R1 = Radiobutton(root, text="Newton", variable=var, value=0)
R2 = Radiobutton(root, text="Lagrange", variable=var, value=1)
L4 = Label(root, text='Result')
L5 = Label(root, text='Time')
L6 = Label(root, text='Polynomial')

is_plot = False


def handle_input(points, degree, value):
    if degree == 0:
        if value > points[len(points) - 1][0]:
            return [points[len(points) - 1]]
        elif value < points[0][0]:
            return [points[0]]
    x = len(points)
    result = []
    if x > degree + 1 > 0:
        left = 1
        right = x - 1
        while left <= right:
            mid = int((left + right) / 2)
            y = mid - degree / 2
            z = y + degree + 1
            if y < 0:
                y = 0
                z = y + degree + 1
            if z > x:
                y = z - degree - 1

            if points[mid][0] > value > points[mid - 1][0]:
                break
            elif value < points[mid][0]:
                if right != mid:
                    right = mid
                else:
                    break
            else:
                left = mid + 1
                if left == x:
                    break
    else:
        return points
    for i in range(int(y), int(z), 1):
        result.append(points[i])
    return result


def extract_input(is_plot):
    values = T1.get()
    values = values.split(' ')
    points = []
    for i in range(0, len(values), 2):
        points.append((int(values[i]), int(values[i + 1])))
    if is_plot:
        return points
    points = handle_input(points, int(T3.get()), int(T2.get()))
    return points


def solve():
    try:
        x = int(T2.get())
        points = extract_input(False)
        if var.get() == 0:
            answer = NewtonInterpolation.interpolate(points, x)
            L4.configure(text=answer[0])
            L5.configure(text=answer[2])
            L6.configure(text=answer[1])
            points.append((x, answer[0]))
            points.sort()
            PolynomialPlot.plot(points)
        else:
            answer = lagrangeInterpolation.interpolate(extract_input(False), x)
            L4.configure(text=answer[0])
            L5.configure(text=answer[1])
            L6.configure(text="Polynomial")
            points.append((x, answer[0]))
            points.sort()
            PolynomialPlot.plot(points)
    except:
        warnings.warn("Error")


def plot():
    try:
        PolynomialPlot.plot(extract_input(True))
        L4.configure(text="Result")
        L5.configure(text="Time")
        L6.configure(text="Polynomial")
    except:
        warnings.warn("Error")


def open_file():
    file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if file is not None:
        content = file.read()
        content = content.split('/')
        T1.insert(0, content[0])
        T2.insert(0, content[1])
        T3.insert(0, content[2].split('\n')[0])


B1 = Button(root, text='from file', width=10, command=lambda: open_file())
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
