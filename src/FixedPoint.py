import Function


def fixed_point(xo, eps, n, g):
    if n is None:
        n = 50
    if eps is None:
        eps = 0.00001
    current_eps = 65868541546874571685758714357356413541255000000135405
    xr = xo
    root = []
    for i in range(1, n):
        xr = Function.function_evaluator(g, xr_old)
        if i > 1:
            current_eps = abs((xr - xr_old) / xr)
            if current_eps < eps:
                root.append((i, xr, current_eps))
                break
        root.append((i, xr, current_eps))
        xr_old = xr
    return root
