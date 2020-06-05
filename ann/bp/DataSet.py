import tensorflow as tf
import numpy as np
from PIL import Image


# 将每个图片数据格式化为784*1的numpy数组，标签数据格式化为10*1的numpy数组，便于计算损失函数
def load_data(is_load_train_data):
    image_size = 28
    # 为了避免数据的溢出，需要对照片的每一个值除以2550
    threshold = 2550.0
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
    return (images / threshold), labels


def save_image():
    minist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = minist.load_data()
    img = Image.fromarray(x_train[666].reshape(28, 28), 'L')
    img.save('./image.png')


if __name__ == '__main__':
    save_image()
