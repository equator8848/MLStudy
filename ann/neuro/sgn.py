# coding:utf-8
# Created by Equator at 2019/10/5
import math


def sng_a(net):
    if net >= 0:
        return 1
    else:
        return 0


def sng_b(net):
    if net >= 0:
        return 1
    else:
        return -1


def sng_c(net):
    if net <= 0:
        return 0
    elif net <= 1:
        return net
    else:
        return 1


def sng_d(net):
    if net <= -1:
        return -1
    elif net <= 1:
        return net
    else:
        return 1


# Relu
def sng_e(net):
    if net < 0:
        return 0
    else:
        return net


# Simoid
def sng_f(net):
    return 1/(1+math.pow(math.e, -net))


# 双曲正弦
def sng_g(net):
    return (math.pow(math.e, net) - math.pow(math.e, -net))/(math.pow(math.e, net) + math.pow(math.e, -net))


def factory(flag, net):
    if flag == 'a':
        return sng_a(net)
    elif flag == 'b':
        return sng_b(net)
    elif flag == 'c':
        return sng_c(net)
    elif flag == 'd':
        return sng_d(net)
    elif flag == 'e':
        return sng_e(net)
    elif flag == 'f':
        return sng_f(net)
    elif flag == 'g':
        return sng_g(net)
    else:
        return None
