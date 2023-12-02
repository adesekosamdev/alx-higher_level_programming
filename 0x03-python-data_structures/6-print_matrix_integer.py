#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(0, len(matrix)):
            l = len(matrix[i])
            for j in range(0, l - 1):
                print("{:d}".format(matrix[i][j]), end=" ")
            if l > 0:
                print("{:d}".format(matrix[i][l - 1]))
            else:
                print("")
