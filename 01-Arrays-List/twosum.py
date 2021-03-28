#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/9/3 7:11
# @Author:  haiyong
# @File:    twosum.py
class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            dic[target-n] = i

if __name__ == "__main__":
    num = Solution()
    result = num.twoSum([2, 7, 11, -2,15],9)
    print(result)