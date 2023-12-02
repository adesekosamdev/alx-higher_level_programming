#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(0, len(matrix)):
            list_len = len(matrix[i])
            for j in range(0, list_len - 1):
                print("{:d}".format(matrix[i][j]), end=" ")
            if list_len > 0:
                print("{:d}".format(matrix[i][list_len - 1]))
            else:
                print("")
