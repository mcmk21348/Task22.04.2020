#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    a = 'hackerrank'
    index_a = 0
    for c in s:
        if c == a[index_a]:
            index_a += 1
        if index_a == len(a):
            break
    if index_a == len(a):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()
+
        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()