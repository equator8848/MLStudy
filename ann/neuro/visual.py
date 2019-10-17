# coding:utf-8
# Created by Equator at 2019/10/5
import matplotlib.pyplot as plot
import ann.neuro.excitation_function as sgn


if __name__ == '__main__':
    flag = 'g'
    x = []
    y = []
    left = -10
    right = 10
    i = left
    while i <= 10:
        x.append(i)
        y.append(sgn.factory(flag, i))
        i = i + 0.1
    plot.title('sgn visual')
    plot.plot(x, y, label='sgn')
    # 网格
    plot.grid()
    plot.show()



