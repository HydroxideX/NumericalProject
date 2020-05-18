import Function
import Derivative


def newton_raphson(xo, eps, n, func):
    if n is None:
        n = 50
    if eps is None:
        eps = 0.00001
    current_eps = 65868541546874571685758714357356413541255000000135405
    root = []
    xr = xo
    for i in range(1, n):
        xr_old = xr
        dx = Derivative.get_derivative(func)
        dx_val = Function.function_evaluator(str(dx), xr_old)
        xr = xr_old - (Function.function_evaluator(func, xr_old) / dx_val)
        if i > 1:
            current_eps = (xr - xr_old) / xr
            if current_eps < eps:
                root.append((i, xr, current_eps))
                break
        root.append((i, xr, current_eps))
    return root
