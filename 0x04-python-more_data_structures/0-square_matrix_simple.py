#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        result.append(list(map((lambda x: x * x), i)))
    return result
