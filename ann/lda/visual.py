# coding:utf-8
# Created by Equator at 2019/12/15
from matplotlib import pyplot as plt

if __name__ == '__main__':
    color = ['red', 'blue', 'green']
    marker = ['*', 'o', '^']
    plt.figure()
    plt.title('* is class 1, o is class 2')
    plt.scatter(5, 5, c='red', marker='*')
    plt.show()
