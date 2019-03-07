#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    exit()

argdict = {}
for arg in sys.argv[1:]:
    list1 = arg.split(':')
    key,value = list1
    argdict[key] = value
for key,value in argdict.items():
    print("ID:{} Name:{}".format(key,value))
