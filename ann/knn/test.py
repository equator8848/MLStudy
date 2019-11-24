# coding:utf-8
# Created by Equator at 2019/11/24
import random


def test1():
    sort_container = []
    sort_container_max_size = 5
    size = 10
    for i in range(size):
        num = random.randint(0, 10)
        print(num)
        if len(sort_container) == 0:
            sort_container.append(num)
            continue
        for inx, val in enumerate(sort_container):
            if num > val:
                sort_container.insert(inx, num)
                break
        sort_container.append(num)
    if len(sort_container) > sort_container_max_size:
        print(sort_container)
        sort_container = sort_container[0:sort_container_max_size]
    print(sort_container)


def test2(ref):
    print(ref)
    ref.append(666)
    print(ref)


if __name__ == '__main__':
    li = [1, 3, 5, 7]
    test2(li)
    print(li)
