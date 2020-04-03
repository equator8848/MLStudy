# coding:utf-8
# Created by Equator at 2019/12/15
import random
import math
from matplotlib import pyplot as plt
import numpy as np

class_size = 20
class_num = 2


def init_data():
    points_set = []
    point_set1 = []

    for i in range(class_size):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        point_set1.append((x, y, 1))
    points_set.append(point_set1)

    point_set2 = []
    for i in range(class_size):
        x = random.randint(10, 20)
        y = random.randint(10, 20)
        point_set2.append((x, y, 2))
    points_set.append(point_set2)
    return points_set


def visual(points):
    color = ['red', 'blue', 'green']
    marker = ['*', 'o', '^']
    plt.figure()
    plt.title('* is class 1, o is class 2')
    for inx, sub_points_set in enumerate(points):
        x = [point[0] for point in sub_points_set]
        y = [point[1] for point in sub_points_set]
        plt.scatter(x, y, c=color[inx], marker=marker[inx])
    plt.show()


if __name__ == '__main__':
    points = init_data()
    # visual(points)
    u = [0, 0]
    ui = [[0, 0], [0, 0]]
    for class_i in range(class_num):
        for point_j in points[class_i]:
            ui[class_i][0] = ui[class_i][0] + point_j[0]
            ui[class_i][1] = ui[class_i][1] + point_j[1]
            u[0] = u[0] + point_j[0]
            u[1] = u[1] + point_j[1]
    u = u[0] / (class_num * class_size), u[1] / (class_num * class_size)
    for class_i in range(class_num):
        ui[class_i][0] = ui[class_i][0] / class_size
        ui[class_i][1] = ui[class_i][1] / class_size
    print(u, ui)

    Sb = np.zeros((2, 2))
    for class_i in range(class_num):
        Sb = Sb + len(points[class_i]) * np.dot(
            np.asarray(np.asarray(ui[class_i]).reshape(2, 1) - np.asarray(u).reshape(2, 1)),
            np.asarray(np.asarray(ui[class_i]).reshape(2, 1) - np.asarray(u).reshape(2, 1)).T)
    Sb = Sb / (class_size * class_num)
    print("Sb", Sb)
    Sw = np.zeros((2, 2))
    for class_i in range(class_num):
        temp = np.zeros((2, 2))
        for point_j in points[class_i]:
            temp = temp + np.dot(np.asarray(
                (np.asarray(ui[class_i]).reshape(2, 1) - np.asarray((point_j[0], point_j[1])).reshape(2, 1))),
                np.asarray((np.asarray(ui[class_i]).reshape(2, 1) - np.asarray(
                    (point_j[0], point_j[1])).reshape(2, 1))).T)
        Sw = Sw + len(points[class_i]) * temp
    Sw = Sw / class_size * class_num
    print("Sw", Sw)
    L = np.dot(np.linalg.inv(Sw), Sb)
    print("L", L)
    a, b = np.linalg.eig(L)
    print("a", a, "b", b)
    p = None
    if a[0] > a[1]:
        p = b[:, 0]
    else:
        p = b[:, 1]
    print(p)
    k = p[1] / p[0]
    xp = np.linspace(0, 20, 50)
    yp = k * xp
    # 可视化
    color = ['red', 'blue', 'green']
    marker = ['*', 'o', '^']
    plt.figure()
    plt.title('* is class 1, o is class 2')
    plt.plot(xp, yp, color='green')
    for inx, sub_points_set in enumerate(points):
        x = [point[0] for point in sub_points_set]
        y = [point[1] for point in sub_points_set]
        plt.scatter(x, y, c=color[inx], marker=marker[inx])
    # (x1,y1)线上，(x2,y2)线外
    # x = (y2 - y1 + k * x1 + x2 / k) / (k + 1.0 / k)
    # y = y1 + k * (x - x1)
    for class_i in range(class_num):
        for point_j in points[class_i]:
            x = (point_j[1] - yp + k * xp + point_j[0] / k) / (k + 1.0 / k)
            y = yp + k * (x - xp)
            if point_j[2] == 1:
                plt.scatter(x, y, c='black', marker='>')
            else:
                plt.scatter(x, y, c='pink', marker='^')
    plt.show()
