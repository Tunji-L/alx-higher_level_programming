#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        i_matrix = []
        for j in i:
            j = j * j
            i_matrix.append(j)
        new_matrix.append(i_matrix)
    return(new_matrix)
