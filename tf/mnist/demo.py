import os
import random

import numpy as np
import sys
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
import time
import matplotlib.pyplot as plt


# 计算准确率
def compute_accuracy(v_xs, v_ys):
    global predict
    y_pre = sess.run(predict, feed_dict={x_train: v_xs, keep_drop: 1})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={x_train: v_xs, y_train: v_ys, keep_drop: 1})
    return result


# 创建权重变量
def weight_variable(shape):
    initial = tf.random.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


# 创建偏置变量
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 卷积 padding采用的方式是SAME，不改变输入的大小
def conv(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


# 2*2 最大池化
def max_pool(x):
    return tf.nn.max_pool2d(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def visual(x, y):
    plt.plot(x, y, 'go-')
    plt.title('Accuracy')
    plt.xlabel('index')
    plt.ylabel('accuracy')
    plt.show()


def get_test_data_batch(batch_size):
    global mnist
    temp_x = []
    temp_y = []
    for i in range(batch_size):
        idx = random.randint(0, 9999)
        temp_x.append(mnist.test.images[idx])
        temp_y.append(mnist.test.labels[idx])
    return np.array(temp_x), np.array(temp_y)


# 定义训练集占位符
x_train = tf.compat.v1.placeholder(tf.float32, [None, 784])
y_train = tf.compat.v1.placeholder(tf.float32, [None, 10])
# 定义dropout占位符，防止过拟合
keep_drop = tf.compat.v1.placeholder(tf.float32)
x_image = tf.reshape(x_train, [-1, 28, 28, 1])

# 第一层卷积层
convolution_weight1 = weight_variable([5, 5, 1, 32])
convolution_bias1 = bias_variable([32])
convolution_feature1 = tf.nn.relu(conv(x_image, convolution_weight1) + convolution_bias1)
pooling_result1 = max_pool(convolution_feature1)

# 第二层卷积层
convolution_weight2 = weight_variable([5, 5, 32, 64])
convolution_bias2 = bias_variable([64])
convolution_feature2 = tf.nn.relu(conv(pooling_result1, convolution_weight2) + convolution_bias2)
pooling_result2 = max_pool(convolution_feature2)

# 第一层全连接层
full_weight1 = weight_variable([7 * 7 * 64, 1024])
full_bias1 = bias_variable([1024])
# 展开
pooling_result2_flat = tf.reshape(pooling_result2, [-1, 7 * 7 * 64])
incentive_result1 = tf.nn.relu(tf.matmul(pooling_result2_flat, full_weight1) + full_bias1)
incentive_result1_dropout = tf.nn.dropout(incentive_result1, rate=1 - keep_drop)

# 第二层全连接层
full_weight2 = weight_variable([1024, 10])
full_bias2 = bias_variable([10])
predict = tf.nn.softmax(tf.matmul(incentive_result1_dropout, full_weight2) + full_bias2)

# image data
mnist = read_data_sets('MNIST_data', one_hot=True)

# 损失函数
loss = tf.reduce_mean(-tf.reduce_sum(y_train * tf.math.log(predict), reduction_indices=[1]))

# 训练
train_step = tf.compat.v1.train.AdamOptimizer(1e-4).minimize(loss)
# 训练次数
train_times = 512
# 批次规模
batch_size = 1000
# 结果
idx_results = []
accuracy_results = []
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    start_time = time.time()
    for i in range(train_times):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        test_data_x, test_data_y = get_test_data_batch(batch_size)
        acc = compute_accuracy(test_data_x, test_data_y)
        sess.run(train_step, feed_dict={x_train: batch_x, y_train: batch_y, keep_drop: 0.5})
        idx_results.append(i)
        accuracy_results.append(acc)
        print('第%d次训练，准确率%f，耗时%f' % (i, acc, int((time.time() - start_time) * 1000) / 1000))
    visual(idx_results, accuracy_results)
