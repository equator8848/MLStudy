# coding:utf-8
# Created by Equator at 2019/10/27
import numpy as np
import random
import ann.mnist.MatrixSigmoid as ms
import LoggerConfiguration
import logging


# 隐层与输出层
class Layer:
    def __init__(self, previous_neuron_size, neuron_size):
        self.previous_neuron_size = previous_neuron_size
        self.neuron_size = neuron_size
        self.result = np.zeros((neuron_size, 1))
        # 权重
        self.weight = np.random.rand(neuron_size * previous_neuron_size).reshape(neuron_size, previous_neuron_size)
        # self.weight = np.full((neuron_size, previous_neuron_size), random.random())
        # 偏置（阈值）
        self.bias = np.random.rand(neuron_size).reshape(neuron_size, 1)
        # self.bias = np.full((neuron_size, 1), random.random())
        # 梯度
        # self.grad = np.ones((previous_neuron_size, previous_neuron_size))
        # 局部梯度
        self.local_grad = np.ones((neuron_size, 1))

    # 计算该层的输出
    def calculate(self, previous_neuron_result):
        temp1 = np.matmul(self.weight, previous_neuron_result)
        temp2 = np.add(temp1, self.bias)
        self.result = ms.calculate(temp2)
        return self.result

    # 输出层误差反向传播
    def output_layer_feedback(self, learn_rate, expect_output, previous_neuron_result):
        logging.debug("输出层期望输出 %s" % expect_output.T)
        # 局部梯度（10,1）
        self.local_grad = -(expect_output - self.result) * self.result * (1 - self.result)
        # 梯度（10,1）* (16,1)^T = (10,16)
        grad = self.local_grad * previous_neuron_result.T
        # logging.debug("输出层梯度 %s", grad)
        self.weight = self.weight - learn_rate * grad
        self.bias = self.bias - learn_rate * self.local_grad

    # 隐层误差反向传播
    def hide_layer_feedback(self, learn_rate, previous_neuron_result, next_neuron_grad, next_neuron_weight):
        # (16,1) * (16,1) * ()
        self.local_grad = self.result * (1 - self.result) * (np.matmul(next_neuron_grad.T, next_neuron_weight)).T
        grad = self.local_grad * previous_neuron_result.T
        # logging.debug("隐含层梯度 %s", grad)
        self.weight = self.weight - learn_rate * grad
        self.bias = self.bias - learn_rate * self.local_grad
