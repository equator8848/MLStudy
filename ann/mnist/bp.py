# coding:utf-8
# Created by Equator at 2019/10/27
import tensorflow as tf
import random
import numpy as np
from ann.mnist.Layer import Layer

# 加载并准备MNIST数据集，将样本从整数转换为浮点数
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


# 随机获取指定数量的训练数据
def get_train_batch(size):
    data_size = len(x_train)
    for i in range(size):
        index = random.randint(0, data_size) - 1
        yield x_train[index], y_train[index]


def get_test_batch(size):
    data_size = len(x_test)
    for i in range(size):
        index = random.randint(0, data_size)
        yield x_test[index], y_test[index]


# 将标签复原为矩阵
def get_desired_output(output_size, y_expect):
    output = np.zeros((output_size, 1))
    output[y_expect - 1] = 1
    return output


def find_max(output_size, output):
    max_value = output[0]
    max_index = 0
    for i in range(output_size):
        if output[i] > max_value:
            max_value = output[i]
            max_index = i
    return max_index


def bp():
    learn_rate = 0.01
    # 输入层神经元数量（28*28=784）
    input_layer_size = 784
    # 隐层神经元数量
    hide_layer_size = 16
    # 输出层神经元数量
    output_layer_size = 10
    # 每批数据数据量
    mini_batch_size = 10000

    # 测试数目
    train_size = 100
    train_counter = 0
    # 建立隐层
    hide_layer_list = [Layer(input_layer_size, hide_layer_size), Layer(hide_layer_size, hide_layer_size)]
    # 建立输出层
    output_layer = Layer(hide_layer_size, output_layer_size)

    while train_counter != train_size:
        train_data_rows = get_train_batch(mini_batch_size)
        # 每个训练对
        for train_data_row in train_data_rows:
            x_train_row, y_train_row = train_data_row
            # 将二维数组转换为一维向量
            x_train_row_matrix = np.array(x_train_row)
            # (784,1)
            input_layer = x_train_row_matrix.reshape(input_layer_size, 1)
            for i in range(len(hide_layer_list)):
                # 除第一层隐层外，其余隐层数据输入为上一层的输出
                if i == 0:
                    hide_layer_list[i].calculate(input_layer)
                else:
                    hide_layer_list[i].calculate(hide_layer_list[i - 1].result)
            output_layer.calculate(hide_layer_list[-1].result)

            # 反向传播
            output_layer.output_layer_feedback(learn_rate, get_desired_output(output_layer_size, y_train_row),
                                               hide_layer_list[-1].result)
            # 方向遍历隐含层
            for i in range(len(hide_layer_list) - 1, -1, -1):
                # print("i=%d" % i)
                # 倒数第一层
                if i == len(hide_layer_list) - 1:
                    hide_layer_list[i].hide_layer_feedback(learn_rate, hide_layer_list[i - 1].result,
                                                           output_layer.local_grad, output_layer.weight)
                # 第一层
                elif i == 0:
                    hide_layer_list[i].hide_layer_feedback(learn_rate, input_layer, hide_layer_list[i + 1].local_grad,
                                                           hide_layer_list[i + 1].weight)
                # 其它隐含层
                else:
                    hide_layer_list[i].hide_layer_feedback(learn_rate, hide_layer_list[i - 1].result,
                                                           hide_layer_list[i + 1].local_grad,
                                                           hide_layer_list[i + 1].weight)
        train_counter = train_counter + 1
        print("第%d次训练" % train_counter)
    print("训练结束")

    test_size = 1000
    test_correct_counter = 0

    test_data_rows = get_test_batch(test_size)
    for test_data_row in test_data_rows:
        x_test_row, y_test_row = test_data_row
        # 将二维数组转换为一维向量
        x_test_row_matrix = np.array(x_test_row)
        # (784,1)
        input_layer = x_test_row_matrix.reshape(input_layer_size, 1)
        for i in range(len(hide_layer_list)):
            # 除第一层隐层外，其余隐层数据输入为上一层的输出
            if i == 0:
                hide_layer_list[i].calculate(input_layer)
            else:
                hide_layer_list[i].calculate(hide_layer_list[i - 1].result)
        output_layer.calculate(hide_layer_list[-1].result)
        result = find_max(output_layer_size, output_layer.result)
        if result == y_test_row:
            test_correct_counter = test_correct_counter + 1

    print("正确率：%f" % (test_correct_counter / test_size))


if __name__ == '__main__':
    bp()
