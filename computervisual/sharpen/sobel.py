# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 15:27
# @Author  : Equator
import numpy as np

x_template = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
y_template = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]


def sobel_filter(input_img):
    filter_size = 3
    input_img_cp = np.copy(input_img)
    pad_num = int((filter_size - 1) / 2)
    input_img_cp = np.pad(input_img_cp, (pad_num, pad_num), mode='constant', constant_values=0)
    m, n = input_img_cp.shape
    output_img = np.copy(input_img_cp)
    for i in range(pad_num, m - pad_num):
        for j in range(pad_num, n - pad_num):
            sx = input_img_cp[i - pad_num:i + pad_num + 1, j - pad_num:j + pad_num + 1] * x_template
            sy = input_img_cp[i - pad_num:i + pad_num + 1, j - pad_num:j + pad_num + 1] * y_template
            output_img[i, j] = np.sqrt(np.square(np.sum(sx)) + np.square(np.sum(sy)))
    # 裁剪
    output_img = output_img[pad_num:m - pad_num, pad_num:n - pad_num]
    return output_img
