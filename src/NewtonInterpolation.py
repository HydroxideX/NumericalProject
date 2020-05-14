#call the interpolate function after importing with parameters points (ex: [(1,2),(5,6),(7,8)]) and value ex: 2
#only send the set of points that are needed in the function as the functions use the whole points array in its calculation

import numpy as np
import time


def calculate_value(div_diff_table, points, value):
    answer = 0
    m = div_diff_table.shape[0]
    for i in range(0, m):
        temp = 1
        for j in range(0, i):
            temp *= (value - points[j][0])
        answer += temp*div_diff_table[i][i]
    return answer


def get_polynomial(div_diff_table, points):
    s = ""
    m = div_diff_table.shape[0]
    for i in range(0, m):
        if div_diff_table[i][i] < 0:
            s = s[0:len(s) - 2]
            s += "- "
            s += str(-1 * div_diff_table[i][i])
        else :
            s += str(div_diff_table[i][i])
        for j in range(0, i):
            s += ("(x - " + str(points[j][0]) + ")")
        if i != m-1:
            s += " + "
    return s


def points_different(points):
    for i in range(1, len(points)):
        if points[i][0] == points[i-1][0]:
            return False
    return True


def generate_divided_difference_table(points):
    m = len(points)
    div_diff_table = np.zeros((m, m))
    for i in range(m):
        div_diff_table[i][0] = points[i][1]
    for j in range(1, m):
        for i in range(j, m):
            div_diff_table[i][j] = (div_diff_table[i][j-1] - div_diff_table[i-1][j-1]) / (points[i][0] - points[i-j][0])
    return div_diff_table


def interpolate(points, value):
    current_time = time.time()
    points.sort()
    assert(points_different(points))
    div_diff_table = generate_divided_difference_table(points)
    answer = [calculate_value(div_diff_table, points, value), get_polynomial(div_diff_table, points)]
    exec_time = ((time.time()) - current_time)*1000
    answer.append(exec_time)
    return answer


