# assume f(xl)f(xu)<0
import Function


def bisection(xl, xu, func, eps, n):
    if n is None:
        n = 50
    if eps is None:
        eps = 0.00001
    current_eps = 65868541546874571685758714357356413541255000000135405
    xr = (xl + xu) / 2
    root = []
    for i in range(1, n):
        if (Function.function_evaluator(func, xl) * Function.function_evaluator(func, xr)) < 0:
            xr_old = xr
            xu = xr
        elif Function.function_evaluator(func, xr) * Function.function_evaluator(func, xl) == 0:
            root.append((i, xl, xu, xr, current_eps))
            break
        else:
            xr_old = xr
            xl = xr
        if i > 1:
            current_eps = (xr - xr_old) / xr
            if current_eps < eps:
                root.append((i, xl, xu, xr, current_eps))
                break
        root.append((i, xl, xu, xr, current_eps))
    return root
