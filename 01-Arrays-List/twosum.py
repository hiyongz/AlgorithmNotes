#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/9/3 7:11
# @File:    twosum.py

"""
1. 两数之和
https://leetcode-cn.com/problems/two-sum/
"""

from typing import List

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            dic[target-n] = i

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        index = [[] for _ in range(2)]
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    index[0] = i
                    index[1] = j
                    return index

if __name__ == "__main__":
    num = Solution()
    result = num.twoSum([1, 11, 7, -2,15],9)
    print(result)