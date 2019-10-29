# coding:utf-8
# Created by Equator at 2019/10/27
import numpy as np


def test_a():
    a = [[1, 3, 4, 6, 8]]
    matrix_a = np.asarray(a)
    print(matrix_a)
    print(matrix_a.shape)
    print(matrix_a.T)
    print(matrix_a.T.shape)
    b = [1, 5, 6, 8, 9]
    matrix_b = np.asarray(b)
    print(matrix_b)
    print(matrix_b.shape)
    print(matrix_b.T)
    print(matrix_b.T.shape)
