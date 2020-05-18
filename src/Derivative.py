import sympy as sp
import Function


def get_derivative(func):
    x = sp.Symbol('x')
    dx = sp.diff(func, x)
    return dx

