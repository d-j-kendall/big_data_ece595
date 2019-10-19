#!/usr/bin/python3
import sys
last_user = None
count = 1
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    if line[0] == last_user:
        count = count+1
    else:
        if last_user is not None:
            print(f"{last_user}\t{count}")
        count = 1
        last_user = line[0]

print(f"{last_user}\t{count}")
