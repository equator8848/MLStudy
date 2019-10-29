# coding:utf-8
# Created by Equator at 2019/10/28
import numpy as np

if __name__ == '__main__':
    a = np.ones((10, 1))
    b = np.ones((16, 1))
    c = a * b.T
    print(c)
    print(c.shape)
    d = np.matmul(a, b.T)
    print(d)
    print(d.shape)
    e = b.T * a
    print(e)
    print(e.shape)
