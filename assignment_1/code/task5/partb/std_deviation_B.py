#!/usr/bin/python3
import copy
import math
import ast
import sys
import pdb




def data_mean(purchase_amounts):

    siz = len(purchase_amounts)
    indx = siz - 1
    price = purchase_amounts.pop(indx)
    if indx ==0:
        return price
    else:
        return data_mean(purchase_amounts) * (1 - 1 / siz) + price / siz

for line in sys.stdin.readlines():
    line_dict = ast.literal_eval(line)

    for key, value in line_dict.items():
        value2 = [i**2 for i in value]
        x2 = data_mean(value2)
        x = data_mean(value)
        standard_deviation = math.sqrt(x2-x**2)
        print("%s\t%s" % (key, standard_deviation))
