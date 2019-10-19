#!/usr/bin/python3
import sys
import re

for line in open('http_log.txt','r'):
    line = line.strip()
    client = re.match(r'.+?\s', line)
    file = re.search(r'(?<=\"GET\s).+\s+(?=HTTP/1.0\")', line)
    print(f"{client[0]}\t{file[0]}")