import Function
import Derivative


def secant(x1, x2, n, eps, func):
    if n is None:
        n = 50
    if eps is None:
        eps = 0.00001
    current_eps = 65868541546874571685758714357356413541255000000135405
    root = []
    xr = x2
    for i in range(1, n):
        xr_old = xr
        xr = xr_old - ((Function.function_evaluator(func, xr_old) * (x1 - xr)) / (
                Function.function_evaluator(func, x1) - Function.function_evaluator(func, xr_old)))
        x1 = xr_old
        if i > 1:
            current_eps = abs((xr - xr_old) / xr)
            if current_eps < eps:
                root.append((i, x1, xr_old, xr, current_eps))
                break
        root.append((i, x1, xr_old, xr, current_eps))
    return root
