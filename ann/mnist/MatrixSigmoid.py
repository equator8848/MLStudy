# coding:utf-8
# Created by Equator at 2019/10/27
import ann.neuro.excitation_function as sf
import numpy as np


def calculate(input_matrix):
    results = []
    for data in input_matrix:
        result = sf.factory('f', data)
        results.append(result)
    return np.asarray(results)



