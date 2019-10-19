#!/usr/bin/python3

import os
import sys
import re

for line in sys.stdin:
    line = line.strip()
    wreg = re.compile(r'\w+')
    words = re.findall(wreg, line)
    for word in words:
        print(f"{word.lower()}\t1")
