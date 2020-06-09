# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 22:48
# @Author  : Equator
import numpy as np


def means_filter(input_img, filter_size):
    input_img_cp = np.copy(input_img)
    filter_template = np.ones(filter_size, filter_size)
    pad_num = int((filter_size - 1) / 2)
    input_img_cp = np.pad(input_img_cp, (pad_num, pad_num), mode='constant', constant_values=0)
    m, n = input_img_cp.shape
    output_img = np.copy(input_img)
    for i in range(pad_num, m - pad_num):
        for j in range(pad_num, n - pad_num):
            output_img[i, j] = np.sum(filter_template * input_img_cp[i - pad_num:i + pad_num, j - pad_num:j + pad_num]) \
                               / (filter_size ** 2)
    # 裁剪
    output_img = output_img[pad_num:m - pad_num, pad_num:n - pad_num]
    return output_img
