#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # pass = set(password)
    count=0
    flag=0
    special_characters = "!@#$%^&*()-+"
    
    string_map = (map(ord, password))
    for i in string_map:
        if i in range (65, 90):
            flag=1
            break 
    if flag!=1:
        count+=1
    flag=0    

    for i in string_map:
        if i in range (97, 122):
            flag=1
            break   
    if flag!=1:
        count+=1     

    flag=0
    for i in password:
        res=bool(re.match('^[0-9]+$', i))
        if res==True:
            flag=1
            break
    if flag!=1:
        count+=1
    
    flag=0
    for i in password:
        if i in  special_characters:
            print("inside last")
            flag=1
            break
    if flag!=1:
        count+=1
    
    if len(password)<6: 
        req=6-len(password)   
        if req>count:
            return req
        else:
            return count  
    return count

answer = minimumNumber(3, "zss")

print(answer)                                                                                           