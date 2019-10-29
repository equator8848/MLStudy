# coding:utf-8
# Created by Equator at 2019/10/27
import numpy as np


# 隐层与输出层
class Layer:
    def __init__(self, previous_neuron_size, neuron_size):
        self.previous_neuron_size = previous_neuron_size
        self.neuron_size = neuron_size
        self.result = np.zeros((neuron_size, 1))
        # 权重
        self.weight = np.ones((neuron_size, previous_neuron_size))
        # 偏置（阈值）
        self.bias = np.ones((neuron_size, 1))
        # 梯度
        # self.grad = np.ones((previous_neuron_size, previous_neuron_size))
        # 局部梯度
        self.local_grad = np.ones((neuron_size, 1))

    # 计算该层的输出
    def calculate(self, previous_neuron_result):
        self.result = np.add(np.matmul(self.weight, previous_neuron_result), self.bias)
        return self.result

    # 输出层误差反向传播
    def output_layer_feedback(self, learn_rate, expect_output, previous_neuron_result):
        # 局部梯度（10,1）
        self.local_grad = -(expect_output - self.result) * self.result * (1 - self.result)
        # print("输出层局部梯度", self.local_grad.shape)
        # 梯度（10,1）*(16,1)^T ~ (10,16)
        grad = self.local_grad * previous_neuron_result.T
        # print("输出层梯度", grad.shape)
        self.weight = self.weight - learn_rate * grad

    # 隐层误差反向传播
    def hide_layer_feedback(self, learn_rate, previous_neuron_result, next_neuron_grad, next_neuron_weight):
        # (16,1) * (16,1) * ()
        self.local_grad = self.result * (1 - self.result) * (np.matmul(next_neuron_grad.T, next_neuron_weight)).T
        grad = self.local_grad * previous_neuron_result.T
        self.weight = self.weight - learn_rate * grad
