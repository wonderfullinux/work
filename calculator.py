#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Parameter Error")
    exit()
try:
    gz = int(sys.argv[1])
except ValueError:
    print("Parameter Error")
    exit()

yn = gz - 5000
if yn > 0:
    if yn <= 3000:
        sl = 0.03
        ss = 0
    elif yn > 3000 and yn <= 12000:
        sl = 0.1
        ss = 210
    elif yn > 12000 and yn <= 25000:
        sl = 0.2
        ss = 1410
    elif yn > 25000 and yn <= 35000:
        sl = 0.25
        ss = 2660
    elif yn > 35000 and yn <= 55000:
        sl = 0.3
        ss = 4410
    elif yn > 55000 and yn <= 80000:
        sl = 0.35
        ss = 7160
    elif yn > 80000:
        sl = 0.45
        ss = 15160
    ns = yn * sl - ss
    print('{:.2f}'.format(ns))
else:
    print("0.00")


