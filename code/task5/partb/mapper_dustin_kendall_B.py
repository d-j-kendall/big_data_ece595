#!/usr/bin/python3
import sys
import os

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    city = line[2]
    amount = line[4]
    print("%s\t%s"%(city, amount))
