#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    count=0
    for i in s:
        num=ord(i)
        if num in range(65, 91):
            print("inside count")
            count+=1
    return count+1            


result = camelcase("saveChangesInTheEditor")
print(result)