#!/usr/bin/env python3

import sys

def calculator(gz):
    yn = gz - 0.165 * gz - 5000
    if yn <= 0:
        ns = 0 
    elif yn <= 3000:
        ns = yn * 0.03 
    elif yn <= 12000:
        ns = yn * 0.1 - 210
    elif yn <= 25000:
        ns = yn * 0.2 - 1410
    elif yn <= 35000:
        ns = yn * 0.25 - 2660
    elif yn <= 55000:
        ns = yn * 0.3 - 4410
    elif yn <= 80000:
        ns = yn * 0.35 - 7160
    else:
        ns = yn * 0.45 - 15160
    sh = gz - 0.165 * gz - ns
    return sh

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Parameter Error")
        exit()
    
    dict1 = {}
    for arg in sys.argv[1:]:
        key, value = arg.split(':')
        try:
            dict1[int(key)] = int(float(value))
        except ValueError:
            print("Parameter Error")
            exit()

    for gh, gz in dict1.items():
        print("{}:{:.2f}".format(gh, calculator(gz)))


