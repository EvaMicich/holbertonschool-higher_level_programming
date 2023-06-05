#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        matrix = [[]]
    if matrix == [[]] or matrix == [] or matrix == "":
        print("")
        return
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == len(matrix[i]) - 1:
                    print("{}".format(matrix[i][j]))
                else:
                    print("{}".format(matrix[i][j]), end=" ")
