# coding:utf-8
import random
import math
from matplotlib import pyplot as plt

k = 7


def init_data():
    points_set = []
    point_set1 = [(3, 1, 1), (2, 5, 1), (1, 2, 1), (2, 2, 1), (1, 7, 1), (1, 6, 1), (3, 7, 1), (5, 4, 1), (2, 1, 1),
                  (5, 2, 1)]
    points_set.append(point_set1)
    point_set2 = [(10, 5, 2), (9, 8, 2), (6, 10, 2), (4, 9, 2), (9, 10, 2), (10, 6, 2), (5, 7, 2), (6, 4, 2), (8, 6, 2),
                  (8, 7, 2), (10, 9, 2), (10, 10, 2), (7, 10, 2), (10, 9, 2)]
    points_set.append(point_set2)
    return points_set


def visual(points):
    color = ['blue', 'green']
    marker = ['*', '+']

    plt.figure()
    plt.title('* is class -, + is class +')
    for inx, sub_points_set in enumerate(points):
        x = [point[0] for point in sub_points_set]
        y = [point[1] for point in sub_points_set]
        plt.scatter(x, y, c=color[inx], marker=marker[inx])
    plt.show()


def visual_with_unknown_point(points, unknown_point):
    color = ['blue', 'green']
    marker = ['*', '+']

    plt.figure()
    plt.title('* is class -, + is class +')
    for inx, sub_points_set in enumerate(points):
        x = [point[0] for point in sub_points_set]
        y = [point[1] for point in sub_points_set]
        plt.scatter(x, y, c=color[inx], marker=marker[inx])
    plt.scatter(unknown_point[0], unknown_point[1], c='red', label='unknown')
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
    dist = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))
    print("(%d,%d)与(%d,%d)的欧氏距离为%f" % (p1[0], p1[1], p2[0], p2[1], dist))
    return dist


def vote(distance_label_list):
    print(distance_label_list)
    label1 = 0
    label2 = 0
    for distance_label in distance_label_list:
        if distance_label[1] == 1:
            label1 = label1 + 1
        elif distance_label[1] == 2:
            label2 = label2 + 1
        else:
            pass
    if label1 > label2:
        return 1
    elif label1 < label2:
        return 2
    else:
        return 0


if __name__ == '__main__':
    points = init_data()
    # visual(points)
    unknown_point = (4, 8)
    distance_label_list = []
    for point in list_translate(points):
        dis = distance(point, unknown_point)
        sort_util(distance_label_list, (dis, point[2]))
        if len(distance_label_list) > k:
            distance_label_list = distance_label_list[0:k]
    result = vote(distance_label_list)
    if result == 1:
        print("预测结果为：+类")
    elif result== 2:
        print("预测结果为：-类")
    else:
        print("平票")
    visual_with_unknown_point(points, unknown_point)
