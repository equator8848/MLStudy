# coding:utf-8
# Created by Equator at 2019/10/5
import numpy as np
import ann.neuro.sgn as sgn

# 统一阈值模型
if __name__ == '__main__':
    # 权值输入（其中W0为阈值）
    input_w = [1, 3, 5, 7, 9]
    W = np.mat(input_w)
    # 输入（其中X0固定为-1）
    inout_x = [-1, 2, 4, 6, 8]
    X = np.mat(inout_x)
    net = np.matmul(W, X.T)
    o = sgn.factory('a', net)
    print(o)



