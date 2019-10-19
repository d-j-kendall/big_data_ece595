#!/usr/bin/python3

import sys
import re
last_key, last_value = None, None
for line in sys.stdin:
    key, value = line.split('\t')
    if last_key is None:
        last_key = key
        last_value = int(value)
    elif last_key != key:
        print(f"{last_key}\t{last_value}")
        last_key = key
        last_value = int(value)
    else:
        last_value = last_value + int(value)

print(f"{last_key}\t{last_value}")
