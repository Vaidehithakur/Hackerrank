#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def diagonalDifference(grades):
    primary_diagonal_sum=0
    secondary_diagonal_sum=0
    for index_i,i in enumerate(arr):
            for index_j,j in enumerate (i):
                if index_i==index_j:
                    primary_diagonal_sum+=arr[index_i][index_j]
                if index_j==(len(arr[0])-1)-index_i:
                    secondary_diagonal_sum+=arr[index_i][index_j]
    return abs(secondary_diagonal_sum-primary_diagonal_sum)

arr = [[0, 2, 4 ], [4, 7, 1], [0, 1, 3]]
result = diagonalDifference(arr)
print(result)