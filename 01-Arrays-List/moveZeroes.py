#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
283. 移动零
https://leetcode-cn.com/problems/move-zeroes/
"""

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j = j + 1
        return nums
if __name__ == "__main__":
    num = Solution()
    result = num.moveZeroes([0,1,0,3,12])
    print(result)