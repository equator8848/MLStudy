# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 16:17
# @Author  : Equator

import matplotlib.pyplot as plt


def img_compare(img_map):
    plt.title('img_compare')
    i = 1
    for key in img_map:
        plt.subplot(len(img_map), 1, i)
        plt.imshow(img_map[key])
        i = i + 1
    plt.show()
