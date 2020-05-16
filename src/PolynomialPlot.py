# call the plot function after importing with parameters points (ex: [(1,2),(5,6),(7,8)])
# only send the set of points that are needed in the function as the functions use the whole points array in its calculation

import numpy as np
from matplotlib import pyplot as plt


def solve_polynomial(A, b):
    multiplication = np.dot(np.linalg.inv(A), b)
    l = multiplication.reshape(1, multiplication.shape[0])
    return l


def generate_array(points):
    m = len(points)
    A = np.ones((m, m))
    b = np.zeros((m, 1))
    for i in range(0, m):
        b[i][0] = points[i][1]
        A[i][1] = points[i][0]
    for j in range(2, m):
        for i in range(0, m):
            A[i][j] = A[i][1] ** j
    return A, b


def plot(points):
    A, b = generate_array(points)
    coefficients = solve_polynomial(A, b)
    x = np.zeros((1, len(points)))
    for i in range(len(points)):
        x[0][i] = points[i][0]
    coefficients = coefficients.reshape(coefficients.shape[1])
    coefficients = coefficients[::-1]
    xi = np.linspace(points[0][0], points[len(points) - 1][0])
    poly = np.poly1d(coefficients)
    plt.plot(xi, poly(xi))
    plt.show()


points = [(1, 0), (4, 1.386), (6, 1.791)]
plot(points)
