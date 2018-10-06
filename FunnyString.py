#!/bin/python

import math
import os
import random
import re
import sys

def calculate_ascii_difference(s):
    temp=0
    actual_list=[]
    for i in s:
        if temp!=0:
            actual_list.append(abs(ord(i)-temp))
        temp=ord(i)
    return actual_list      

# Complete the funnyString function below.
def funnyString(s):
    flag=0
    str=""
    for i in s:
        str=i+str
    list_s=calculate_ascii_difference(s)        
    l1=list(reversed(list_s))
    for (i,j) in zip(list_s, l1):
        if i!=j:
            flag=1
            break
    if flag==1:
        return "Not Funny"
    return "Funny"

result = funnyString("abbbas")
print(result)

