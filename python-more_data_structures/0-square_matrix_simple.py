#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sublist in matrix:
        new_sublist = [number ** 2 for number in sublist]
        new_matrix.append(new_sublist)
    return new_matrix
