# coding:utf-8
# Created by Equator at 2019/10/5
import math

# excitation function 激励函数


def ef_a(net):
    if net >= 0:
        return 1
    else:
        return 0


def ef_b(net):
    if net >= 0:
        return 1
    else:
        return -1


def ef_c(net):
    if net <= 0:
        return 0
    elif net <= 1:
        return net
    else:
        return 1


def ef_d(net):
    if net <= -1:
        return -1
    elif net <= 1:
        return net
    else:
        return 1


# Relu
def ef_e(net):
    if net < 0:
        return 0
    else:
        return net


# Simoid
def ef_f(net):
    return 1/(1+math.pow(math.e, -net))


# 双曲正弦
def ef_g(net):
    return (math.pow(math.e, net) - math.pow(math.e, -net))/(math.pow(math.e, net) + math.pow(math.e, -net))


def factory(flag, net):
    if flag == 'a':
        return ef_a(net)
    elif flag == 'b':
        return ef_b(net)
    elif flag == 'c':
        return ef_c(net)
    elif flag == 'd':
        return ef_d(net)
    elif flag == 'e':
        return ef_e(net)
    elif flag == 'f':
        return ef_f(net)
    elif flag == 'g':
        return ef_g(net)
    else:
        return None
