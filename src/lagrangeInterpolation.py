#call the interpolate function after importing with parameters points (ex: [(1,2),(5,6),(7,8)]) and value (ex: 2)
#only send the set of points that are needed in the function as the functions use the whole points array in its calculation

import time



def calculate_value(points, value):
    answer = 0
    m = len(points)
    for i in range(m):
        temp = 1
        for j in range(m):
            if j == i:
                continue
            temp *= ((value - points[j][0])/(points[i][0] - points[j][0]))
        answer += temp * points[i][1]
    return answer


def points_different(points):
    for i in range(1, len(points)):
        if points[i][0] == points[i-1][0]:
            return False
    return True


def interpolate(points, value):
    current_time = time.time()
    points.sort()
    assert(points_different(points))
    answer = [calculate_value(points, value)]
    exec_time = ((time.time()) - current_time)*1000
    answer.append(exec_time)
    return answer


