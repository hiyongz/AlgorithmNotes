#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/11/10 17:07
# @Author:  haiyong
# @File:    test.py

class Solution:
    def fib(self, n):
        cash = {0:0,1:1}
        def memoize(n):
            if n in cash:
                return cash[n]
            cash[n] = memoize(n - 1) + memoize(n - 2)
            return cash[n]
        return memoize(n)
if __name__ == "__main__":
    solu = Solution()
    result = solu.fib(10)
    print(result)