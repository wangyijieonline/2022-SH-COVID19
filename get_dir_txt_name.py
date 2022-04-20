# -*- coding: utf-8 -*-

import os, sys

# open the dir
path = "rawdata"
dirs = os.listdir(path)

# list all files
for file in dirs:
   print(file)