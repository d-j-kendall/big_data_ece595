#!/usr/bin/python3
import os, sys

purchase_list = {}

last_city = None
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    if line[0] == last_city:
        purchase_list[str(last_city)].append(float(line[1]))
    else:
        last_city = line[0]
        purchase_list[last_city] = [float(line[1])]

print(purchase_list)
