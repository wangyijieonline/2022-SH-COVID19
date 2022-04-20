# -*- coding: utf-8 -*-
import os, sys

filename = 'rawdata/0418.txt'
f = open(filename, encoding='utf-8')

while True:
    line = f.readline()
    if line:
        # print (line)
        if '居住于' in line:
            content = line.replace('病例', '', 2)
            content = content.replace('居住于', '', 1)
            content = content.replace('无症状感染者', '', 2)
            content = content.replace('—', ' ', 1)
            content = content.replace('、', ' ', 1)
            content = content.replace('，', ' ', 2)
            print(content, end="")
    else:
        break
    
f.close()