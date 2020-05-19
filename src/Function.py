from math import *


def function_evaluator(func, x):
    # expression to be evaluated
    expr = func

    # evaluating expression
    y = eval(expr)

    return y


print(function_evaluator('sin(x)', 1))
