import numpy as np
import matplotlib.pyplot as plt
import Function


def graph(formula, x_range):
    x1 = np.array(x_range)
    # y = eval(formula)
    y = []
    for i in range(len(x1)):
        x = x1[i]
        y.append(Function.function_evaluator(str(formula), x))

    plt.plot(x1, y)
    plt.show()


graph('sin(x)', range(-4,20))
