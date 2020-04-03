import tensorflow as tf
import numpy as np


# 将每个图片数据格式化为784*1的numpy数组，标签数据格式化为10*1的numpy数组
def load_data(is_load_train_data=True):
    image_size = 28
    threshold = 255.0
    minist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = minist.load_data()
    if is_load_train_data:
        images = x_train
        labels = y_train
    else:
        images = x_test
        labels = y_test
    images = images.reshape(len(labels), image_size * image_size)
    ls = []
    for label in labels:
        temp = np.zeros(10)
        temp[label] = 1
        ls.append(temp.T)
    labels = np.array(ls)
    return images / threshold, labels


if __name__ == '__main__':
    images, labels = load_data()
    print(images.shape)
    print(labels.shape)
