# link: https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 or (6 <= n <= 20 and n % 2 == 0):
        print('Weird')
    else:
        print('Not Weird')