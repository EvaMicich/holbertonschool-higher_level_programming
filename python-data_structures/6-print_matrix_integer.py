#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        matrix = [[]]
    if matrix == [[]] or matrix == [] or matrix == "":
        print("")
        return
    else:
        for i in matrix:
            print("{}".format(i))
