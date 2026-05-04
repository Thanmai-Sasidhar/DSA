#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#
from collections import deque

def solve(arr, queries):
    result = []
    n = len(arr)

    for d in queries:
        if d == 0:
            result.append(0)
            continue

        dq = deque()
        window_max = []

        for i in range(n):
            # Remove elements smaller than current
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Remove elements out of window
            if dq[0] <= i - d:
                dq.popleft()

            # Store max of window
            if i >= d - 1:
                window_max.append(arr[dq[0]])

        # Minimum among all window maximums
        result.append(min(window_max) if window_max else 0)

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
