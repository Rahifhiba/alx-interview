#!/usr/bin/python3
""" rotation of matrix """


def rotate_2d_matrix(matrix):
    """rotate the matrix"""
    tmp = matrix
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            matrix[i][j] = tmp[j][i]
