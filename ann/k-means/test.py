# coding:utf-8
# Created by Equator at 2019/11/24

def test1():
    li = [[] for i in range(3)]
    # li = [[], [], []]
    li[0].append(3)
    li[0].append(4)
    print(li)


def test2():
    li = [[1, 5, 9], [2, 6, 8], [7, 8, 9]]
    print([l[0] for l in li])


def test3(li):
    li[2] = 666


if __name__ == '__main__':
    li = [1, 3, 5, 7]
    test3(li)
    print(li)
