#!/usr/bin/python3
import sys
import operator
file = open("reduced_passage.txt",'r')
dic_list = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    kv_pairs = {
        "key": key,
        "value": int(value),
    }
    dic_list.append(kv_pairs)
dic_list.sort(reverse= True,key=operator.itemgetter("value"))
top_ten = dic_list[0:9]
for kv in top_ten:
    print("%s\t%s" % (kv["key"], str(kv["value"])))
