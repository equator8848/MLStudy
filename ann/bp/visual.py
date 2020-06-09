# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 19:45
# @Author  : Equator

from ann.bp import DataSet
from ann.bp.NeuralNetwork import NeuralNetwork
import pandas as pd
import csv


def learn_step_result():
    train_times = 5
    layers = [784, 30, 10]
    steps = [s / 10 + 0.1 for s in range(10)]
    print("学习步长：", steps)
    result = []
    for step in steps:
        network = NeuralNetwork(2, step, layers)
        x_train, y_train = DataSet.load_data(True)
        print("训练环节...")
        for i in range(train_times):
            for j in range(len(x_train)):
                network.update(x_train[j], y_train[j])
        correct_num = 0
        print("测试环节...")
        x_test, y_test = DataSet.load_data(False)
        for i in range(len(y_test)):
            if network.test(x_test[i], y_test[i]):
                correct_num += 1
        correct_rate = correct_num * 100 / len(y_test)
        print("学习步长%f 正确率 %f%%" % (step, correct_rate))
        result.append([step, correct_rate])
        with open('learn_step_result.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(result)


def neurons_number_result():
    train_times = 5
    learn_step = 0.2
    nums = [(s + 1) * 10 for s in range(10)]
    print("神经元个数：", nums)
    result = []
    for num in nums:
        layers = [784, num, 10]
        network = NeuralNetwork(2, learn_step, layers)
        x_train, y_train = DataSet.load_data(True)
        print("训练环节...")
        for i in range(train_times):
            for j in range(len(x_train)):
                network.update(x_train[j], y_train[j])
        correct_num = 0
        print("测试环节...")
        x_test, y_test = DataSet.load_data(False)
        for i in range(len(y_test)):
            if network.test(x_test[i], y_test[i]):
                correct_num += 1
        correct_rate = correct_num * 100 / len(y_test)
        print("神经元个数%d 正确率 %f%%" % (num, correct_rate))
        result.append([num, correct_rate])
        with open('neurons_number.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(result)


def neurons_layer_result():
    train_times = 10
    learn_step = 0.2
    layers = []
    for i in range(5):
        layer = []
        layer.append(784)
        for l in range(i + 1):
            layer.append(30)
        layer.append(10)
        layers.append(layer)
    print("神经元层数：", layers)
    result = []
    for layer in layers:
        network = NeuralNetwork(len(layer) - 1, learn_step, layer)
        x_train, y_train = DataSet.load_data(True)
        print("训练环节...")
        for i in range(train_times):
            for j in range(len(x_train)):
                network.update(x_train[j], y_train[j])
        correct_num = 0
        print("测试环节...")
        x_test, y_test = DataSet.load_data(False)
        for i in range(len(y_test)):
            if network.test(x_test[i], y_test[i]):
                correct_num += 1
        correct_rate = correct_num * 100 / len(y_test)
        print("神经元隐含层层数%d 正确率 %f%%" % (len(layer) - 2, correct_rate))
        result.append([len(layer) - 2, correct_rate])
        with open('neurons_layer.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(result)


if __name__ == '__main__':
    learn_step_result()
    neurons_number_result()
    neurons_layer_result()
