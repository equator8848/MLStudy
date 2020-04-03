import numpy as np


# 复现 https://github.com/Anonymoushhh/BP_neural_network 大佬的代码，并加上自己的注释
class NeuralNetwork:
    def __init__(self, layer_num, learn_step, neuron_num_each_layer):
        # 网络层数，包括输出层
        self.layer_num = layer_num
        # 学习率
        self.learn_step = learn_step
        # 每层的神经元数目（一个list）
        self.neuron_num_each_layer = neuron_num_each_layer
        # 激活函数
        self.active_function = lambda x: 1.0 / (1.0 + np.exp(-x))
        # 神经网络的全部权值都保存于此
        self.weight = []
        # numpy.random.normal函数有三个参数（loc, scale, size），分别代表生成的高斯分布的随机数的均值、方差以及输出的shape
        for i in range(layer_num):
            # self.weight.append(np.random.normal(
            #     0.0, pow(self.neuron_num_each_layer[i + 1], -0.5),
            #     (self.neuron_num_each_layer[i + 1], self.neuron_num_each_layer[i])
            # ))
            # 生成[0,1)之间的数据
            self.weight.append(np.random.random((self.neuron_num_each_layer[i + 1], self.neuron_num_each_layer[i])))
            # self.weight.append(np.zeros((self.neuron_num_each_layer[i + 1], self.neuron_num_each_layer[i])))

    def update(self, train_x, train_y):
        inputs = np.array(train_x, ndmin=2).T
        targets = np.array(train_y, ndmin=2).T
        # 正向传播
        self.outputs = []
        # 输入层的输出就是原始输入
        self.outputs.append(inputs)
        for i in range(self.layer_num):
            temp_inputs = np.dot(self.weight[i], inputs)
            temp_outputs = self.active_function(temp_inputs)
            # 当前层的输出是下一层的输入
            inputs = temp_outputs
            self.outputs.append(temp_outputs)
        # 计算误差
        self.output_errors = []
        for i in range(self.layer_num):
            if i == 0:
                # 输出层的误差=目标值-输出值
                self.output_errors.append(targets - self.outputs[-1])
            else:
                # 隐层的误差=当前隐层与下一层之间的权值矩阵与下一层误差矩阵的乘积
                self.output_errors.append(np.dot((self.weight[self.layer_num - i]).T, self.output_errors[i - 1]))
        # 反向传播
        for i in range(self.layer_num):
            # f(x)* （1-f(x)）即为激活函数 f(x)的导函数，更新过程从后向前进行
            self.weight[self.layer_num - i - 1] += self.learn_step * np.dot(
                (self.output_errors[i] * self.outputs[-1 - i] * (1.0 - self.outputs[-1 - i])),
                np.transpose(self.outputs[-1 - i - 1]))

    def test(self, test_x, test_y):
        inputs = np.array(test_x, ndmin=2).T
        for i in range(self.layer_num):
            temp_inputs = np.dot(self.weight[i], inputs)
            temp_outputs = self.active_function(temp_inputs)
            inputs = temp_outputs
        # 判断输出层最接近1的那个神经元的下标是否与标签中为1（一组标签只有一个1）的那个下标一致
        return list(inputs).index(max(list(inputs))) == list(test_y).index(1)


if __name__ == '__main__':
    li = [1, 6, 5, 78, 7, 9, 6, 4, 5]
    print(li.index(6))
