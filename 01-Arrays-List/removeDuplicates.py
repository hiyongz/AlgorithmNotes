#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/10 19:41
# @Author:  haiyong
# @File:    removeDuplicates.py
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums) - 1:
            if nums[j] == nums[j + 1]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j + 1]
                j += 1
        return i + 1

if __name__ == "__main__":
    num = Solution()
    result = num.removeDuplicates([0,0,1])
    print(result)