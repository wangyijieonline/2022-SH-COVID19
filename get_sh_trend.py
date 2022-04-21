    # -*- coding: utf-8 -*-
import os, sys

filename = 'rawdata/0420.txt'
f = open(filename, encoding='utf-8')

def getalltxt(path):
    # open the dir
    dirs = os.listdir(path)
    # list all files
    for file in dirs:
        print(file)

def get_content():
    while True:
        line = f.readline()
        if line:
            print (line)
        else:
            break

def find_matched_data():
    while True:
        line = f.readline()
        if line:
            # print (line)
            if "居住于" in line:
                print(line)
        else:
            break

def replace_data():
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

if __name__ == '__main__':
    replace_data()
    f.close()