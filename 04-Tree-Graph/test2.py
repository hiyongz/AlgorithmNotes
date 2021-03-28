#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def solve(S, T):
    lenS = len(S)
    lenT = len(T)

    if lenS > lenT:
        str_ary = list(set(list(lenT)))
        str_ary.sort()









# ******************************结束写代码******************************


try:
    S = raw_input()
except:
    S = None

try:
    _T = raw_input()
except:
    _T = None

res = solve(_S, _T)

print str(res) + "\n"