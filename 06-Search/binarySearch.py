#!/usr/bin/python3
#-*-coding:utf-8-*-

# 二分查找

from typing import List

class Solution:
    def binarySearch(self, arr: List[int], target:int):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                # find the target!!  
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1 

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.binarySearch([2, 8, 10, 20, 30, 35, 42, 50, 52, 60],50)
    print(result)