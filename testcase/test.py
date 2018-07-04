#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

input_num = input('input a number:')
maxnum = int(input_num)
for num in range(maxnum):
    str_num = str(num)
    sum = 0
    for i in str_num:
        sum += int(i)**len(str_num)

    if sum == num:
        print('the number '+ str_num + ' is that')
