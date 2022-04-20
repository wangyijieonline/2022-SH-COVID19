# -*- coding: utf-8 -*-
import os, sys

filename = 'rawdata/0418.txt'
f = open(filename, encoding='utf-8')

while True:
    line = f.readline()
    if line:
        # print (line)
        if "居住于" in line:
            print(line)
    else:
        break

f.close()
