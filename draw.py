import cv2
import numpy as np
import sympy
import matplotlib.pyplot as plt
import random

def set_ellipse_parameter(centerX, centerY, radiusX, radiusY, rotation_deg):
    rotate_rad = np.deg2rad(rotation_deg)
    sin_theta = np.sin(rotate_rad)
    cos_theta = np.cos(rotate_rad)

    A = radiusX ** 2 * sin_theta ** 2 + radiusY ** 2 * cos_theta ** 2
    B = 2 * (radiusY ** 2 - radiusX ** 2) * sin_theta * cos_theta
    C = radiusX ** 2 * cos_theta ** 2 + radiusY ** 2 * sin_theta ** 2
    D = -2 * A * centerX - B * centerY
    E = -1 * B * centerX - 2 * C * centerY
    F = A * centerX ** 2 + B * centerX * centerY \
             + C * centerY ** 2 - radiusX ** 2 * radiusY ** 2

    ellipse_parameter = np.zeros((3, 3), dtype=np.float32)
    ellipse_parameter[0, 0] = A
    ellipse_parameter[1, 1] = C
    ellipse_parameter[2, 2] = F
    ellipse_parameter[0, 1] = B / 2.0
    ellipse_parameter[1, 0] = B / 2.0
    ellipse_parameter[0, 2] = D / 2.0
    ellipse_parameter[2, 0] = D / 2.0
    ellipse_parameter[1, 2] = E / 2.0
    ellipse_parameter[2, 1] = E / 2.0

    return ellipse_parameter


if __name__ == '__main__':
    # ellipse = set_ellipse_parameter(0, 0, 5, 3, 0)
    # print ellipse
    # x = sympy.Symbol('x')
    pt = []
    for i in range(200):
        print i
        x = sympy.Symbol('x')
        # y = (np.random.random(1)*3)[0]
        y = random.random()*20
        print y
        # fun = ((225 - 9 * (x ** 2)) / 25) ** 0.5 - y
        fun = ((1600 - 1 * (x ** 2)) / 4) ** 0.5 - y
        px = sympy.solve(fun, x)
        print px
        pt.append([px[0], y])
        pt.append([px[1], y])
        pt.append([px[0], -y])
        pt.append([px[1], -y])
    for i in range(300):
        print i
        y = sympy.Symbol('y')
        # y = (np.random.random(1)*3)[0]
        x = random.random()*40
        print x
        # fun = ((225 - 9 * (x ** 2)) / 25) ** 0.5 - y
        fun = ((1600 - 4 * (y ** 2))) ** 0.5 - x
        py = sympy.solve(fun, y)
        print px
        pt.append([x, py[0]])
        pt.append([-x, py[0]])
        pt.append([x, py[1]])
        pt.append([-x, py[1]])
    # fun = ((225-9*(x**2))/25)**0.5 - 1
    # y = sympy.solve(fun, x)
    # print y[1]
    print pt
    zero = np.array([0], dtype=np.float32)

    with open('point_xyz.txt', 'w') as f:
        for i in range(len(pt)):
            out = str(pt[i][0]) + ' ' + str(pt[i][1]) + ' ' + str(zero[0])
            print out
            f.write(out)
            f.write('\n')


    a = np.loadtxt('point_xyz.txt')
    # print a[0]

    # plot

    point_x = []
    point_y = []
    for i in range(len(pt)):
        point_x.append(pt[i][0])
        point_y.append(pt[i][1])

    plt.scatter(point_x, point_y, s=5)
    plt.show()
