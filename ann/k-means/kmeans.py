# coding:utf-8
# Created by Equator at 2019/11/24
import random
import math
from matplotlib import pyplot as plt

k = 2
area_num = 2
area_size = 15


def init_data():
    points_set = []

    for i in range(area_size):
        x = random.randint(0, 10)
        y = random.randint(10, 20)
        points_set.append((x, y))

    for i in range(area_size):
        x = random.randint(10, 20)
        y = random.randint(0, 10)
        points_set.append((x, y))

    return points_set


def visual_without_label(points):
    plt.figure()

    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y, c='green')

    plt.show()


def visual_with_center_point(points, center_point_set, cluster_center_set):
    color = ['red', 'blue', 'purple']
    marker = ['*', '+', '^']

    plt.figure()

    for inx, val in enumerate(cluster_center_set):
        x = [point[0] for point in val]
        y = [point[1] for point in val]
        plt.scatter(x, y, c=color[inx], marker=marker[inx])

    for inx, val in enumerate(center_point_set):
        plt.scatter(val[0], val[1], c=color[inx], marker=marker[inx], s=200)
    plt.show()


def distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))


def find_min(source_list):
    min_num = source_list[0]
    flag = 0
    for inx, val in enumerate(source_list):
        if min_num > val:
            min_num = val
            flag = inx
    return flag


# 计算聚类中心（返回一个新的聚类中心点）
def cluster_center_calculate(point_set):
    sum_x = 0
    sum_y = 0
    n = len(point_set)
    for point in point_set:
        sum_x = sum_x + point[0]
        sum_y = sum_y + point[1]
    return sum_x / n, sum_y / n


def cluster_center_refresh(cluster_center, cluster_center_set):
    for i in range(k):
        if len(cluster_center_set[i]) > 0:
            cluster_center[i] = cluster_center_calculate(cluster_center_set[i])


# 准则函数（误差平方和），所有对象到其所在聚类中心的距离之和
def criterion_function(cluster_center, cluster_center_set):
    sum_distance = 0
    for cluster_index in range(k):
        for point in cluster_center_set[cluster_index]:
            dis = distance(cluster_center[cluster_index], point)
            sum_distance = sum_distance + dis
    return sum_distance


def division(distances_list):
    # 划分，cluster_center_set 为二维数组
    cluster_center_set = [[] for i in range(k)]
    for i in range(area_num * area_size):
        distances_col = [temp_distance[i] for temp_distance in distances_list]
        class_flag = find_min(distances_col)
        cluster_center_set[class_flag].append(points[i])
    return cluster_center_set


# 计算距离（每个点到聚类中心的距离）
def distance_calculate(cluster_center, points):
    distances_list = []
    for i in range(k):
        distances = []
        for point in points:
            dis = distance(cluster_center[i], point)
            distances.append(dis)
        distances_list.append(distances)
        print(cluster_center[i], distances)
    return distances_list


if __name__ == '__main__':
    points = init_data()
    visual_without_label(points)
    step = 1
    bound = 1

    # 随机生成聚类中心
    cluster_center = []
    for i in range(k):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        cluster_center.append((x, y))

    distances_list = distance_calculate(cluster_center, points)

    # 划分，cluster_center_set 为二维数组
    cluster_center_set = division(distances_list)
    print(cluster_center_set)

    criterion_function_result = criterion_function(cluster_center, cluster_center_set)
    print(criterion_function_result)

    step = step + 1

    # 重新计算中心点
    print(cluster_center)
    cluster_center_refresh(cluster_center, cluster_center_set)
    print(cluster_center)
    visual_with_center_point(points, cluster_center, cluster_center_set)

    criterion_function_result_temp = criterion_function(cluster_center, cluster_center_set)
    while abs(criterion_function_result - criterion_function_result_temp) > bound:
        criterion_function_result = criterion_function_result_temp
        distances_list = distance_calculate(cluster_center, points)
        cluster_center_set = division(distances_list)
        criterion_function_result_temp = criterion_function(cluster_center, cluster_center_set)
        step = step + 1
        visual_with_center_point(points, cluster_center, cluster_center_set)
    print("结束")
    visual_with_center_point(points, cluster_center, cluster_center_set)
