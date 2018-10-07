#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for index, i in enumerate(grades):
        num=i%5
        if i>=38:
            if num>=3:
                grades[index]= (5-num)+i            # lis1.append((5-num)+i)
            else:
                grades[index]= i
        else:
            grades[index]=i

    return grades
        

        


grades = [73, 67, 38, 33]

result = gradingStudents(grades)
print(result)

