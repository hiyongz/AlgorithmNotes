#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/9/3 7:11
# @File:    threeSum.py

"""
15. 三数之和
https://leetcode-cn.com/problems/3sum/
"""

from typing import List

# 排序
# 双指针，两端逼近

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)-2):
            if nums[k] > 0: #排序后，nums[k]最小，所以nums[k]<=0
                break
            if nums[k] == nums[k-1] and k > 0:
                continue    # 去重
            i, j = k+1, len(nums)-1 # 双指针
            while i < j:
                nums_sum = nums[k] + nums[i] + nums[j]
                if nums_sum < 0: # 小于0说明不够，需要增加数，左指针右移
                    i += 1
                elif nums_sum > 0: # 大于0，需要减数，右指针左移
                    j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # 去重
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.threeSum([-3, -2, -2, 11, 4,10,1])
    print(result)