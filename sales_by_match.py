import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair = dict()
    for i in ar:
        if i in pair:
            pair[i] += 1
        else:
            pair[i] = 1
    count = 0
    for key, val in pair.items():
        count += (val//2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
