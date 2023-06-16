#!/usr/bin/python3
"""
Module: 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    arguments:
    matrix: list of lists containing numbers (int/float)
    div: number to divide by (int/float)

    return:
    matrix with result of division
    """

    num_error = "matrix must be a matrix (list of lists) of integers/floats"
    if any(not isinstance(item, (float, int)) for r in matrix for item in r):
        raise TypeError(num_error)

    if len(set(map(len,matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round((element / div), 2) for element in row] for row in matrix]
