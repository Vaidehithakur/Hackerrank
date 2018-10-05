#!/bin/python

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    k = k%26
    caesar_text=''
    for i in s:
        num=ord(i)
        cipher = ord(i)+k
        # check if the character is an alphabet or special character
        if i.isalpha():
            if num in range(65,91):
                if cipher >= 91:
                    cipher = cipher - 26
            if num in range(97,123):
                if cipher >= 123:
                    cipher = cipher - 26
            caesar_text+=chr(cipher)
        #when the charatcer is not an alphabet then simply write the character in the string    
        else:
            caesar_text+=i        
        
    return caesar_text

result = caesarCipher("www.abc.xyz", 87)
print(result)

