# coding:utf-8
# Created by Equator at 2019/11/24
import random
import math
from matplotlib import pyplot as plt

area_size = 15
k = 7


def init_data():
    points_set = []

    point_set1 = []
    for i in range(area_size):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        point_set1.append((x, y, 1))
    points_set.append(point_set1)

    point_set2 = []
    for i in range(area_size):
        x = random.randint(0, 10)
        y = random.randint(10, 20)
        point_set2.append((x, y, 2))
    points_set.append(point_set2)

    point_set3 = []
    for i in range(area_size):
        x = random.randint(10, 20)
        y = random.randint(10, 20)
        point_set3.append((x, y, 3))
    points_set.append(point_set3)

    return points_set


def visual(points):
    color = ['red', 'blue', 'green']
    plt.figure()

    for inx, sub_points_set in enumerate(points):
        x = [point[0] for point in sub_points_set]
        y = [point[1] for point in sub_points_set]
        plt.scatter(x, y, c=color[inx])

    plt.show()


def visual_with_unknown_point(points, unknown_point):
    color = ['yellow', 'blue', 'green']
    plt.figure()

    for inx, sub_points_set in enumerate(points):
        x = [point[0] for point in sub_points_set]
        y = [point[1] for point in sub_points_set]
        plt.scatter(x, y, c=color[inx])
    plt.scatter(unknown_point[0], unknown_point[1], c='red')
    plt.show()


# 二维列表转一维列表
def list_translate(source):
    return sum(source, [])


def sort_util(distance_label_list, distance_label):
    if len(distance_label_list) == 0:
        distance_label_list.append(distance_label)
        return
    for inx, val in enumerate(distance_label_list):
        if distance_label[0] < val[0]:
            distance_label_list.insert(inx, distance_label)
            break
    distance_label_list.append(distance_label)


def distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))


def vote(distance_label_list):
    label1 = 0
    label2 = 0
    label3 = 0
    for distance_label in distance_label_list:
        if distance_label[1] == 1:
            label1 = label1 + 1
        elif distance_label[1] == 2:
            label2 = label2 + 1
        elif distance_label[1] == 3:
            label3 = label3 + 1
        else:
            pass
    if label1 > label2:
        if label1 > label3:
            return 1
        else:
            return 3
    else:
        if label2 > label3:
            return 2
        else:
            return 3


if __name__ == '__main__':
    points = init_data()
    # visual(points)
    unknown_point = (random.randint(0, 20), random.randint(0, 20))
    distance_label_list = []
    for point in list_translate(points):
        dis = distance(point, unknown_point)
        sort_util(distance_label_list, (dis, point[2]))
        if len(distance_label_list) > k:
            distance_label_list = distance_label_list[0:k]
    result = vote(distance_label_list)
    print("预测结果为：第%d类" % result)
    visual_with_unknown_point(points, unknown_point)
