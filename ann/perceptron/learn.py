# coding:utf-8
# Created by Equator at 2019/10/10
import random
import csv
import numpy as np
import ann.neuro.excitation_function as sf


# 感知机学习算法


def get_random_number():
    # [0,1)
    return random.random()


def init_data():
    headers = ['x1', 'x2', 'x3', 'Y']
    rows = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, -1],
        [0, 1, 0, -1],
        [0, 0, 1, -1],
        [0, 0, 0, -1],
    ]
    with open('data.csv', 'w', newline='') as data:
        w = csv.writer(data)
        # w.writerow(headers)
        w.writerows(rows)


def get_data_from_file():
    with open('./data.csv') as data:
        rows = csv.reader(data)
        result = []
        for row in rows:
            row_list = []
            for dig in row:
                row_list.append(int(dig))
            result.append(row_list)
        print(result)
        return result


# 判断实际输出与理想输出是否一致
def judge(w, dimension, input_rows):
    for row in input_rows:
        result = sir(w, row[0:dimension])
        if result != row[dimension]:
            print(row)
            print('预期输出：' + str(row[dimension]) + '    实际输出：' + str(result))
            return False
    return True


# 感知机，w 权值输入（其中W0为阈值）
def sir(w, input_data):
    W = np.mat(w)
    # 输入（其中X0固定为-1）
    input_data.insert(0, -1)
    X = np.mat(input_data)
    net = np.matmul(W, X.T)
    result = sf.factory('b', net)
    # print('感知机输出结果：' + str(result))
    return result


def learn():
    # 权值|输入变量数
    dimension = 3
    # 数据输入
    input_rows = get_data_from_file()
    # 学习步长
    step = 0.0001
    # 调整次数
    counter = 0
    # 权值向量
    w_list = []
    w0 = []
    i = 0
    # while i <= dimension:
    #     w0.append(get_random_number())
    #     i = i + 1
    w_list.append([0.4, 1, 1, 1])
    while not judge(w_list[counter], dimension, input_rows):
        for row in input_rows:
            # print(row)
            # print(row[0:dimension])
            # print(w_list[counter])
            temp_result = sir(w_list[counter], row[0:dimension])
            w_temp = []
            for i in range(dimension + 1):
                w_temp.append(w_list[counter][i] + step * (row[dimension] - temp_result) * row[i])
            print(w_temp)
            w_list.append(w_temp)
            counter = counter + 1
        print('调整次数：' + str(counter))


if __name__ == '__main__':
    learn()
