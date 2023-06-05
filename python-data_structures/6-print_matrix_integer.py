#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        matrix = [[]]
    if matrix == [[]] or matrix == [] or matrix == "":
        print("")
        return
    else:
        for i in range(len(matrix)):
            row_str = " ".join(str(matrix[i][j]) for j in range(len(matrix[i])))
            print(row_str)
