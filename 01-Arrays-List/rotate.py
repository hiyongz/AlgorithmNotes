
"""
189. 旋转数组
https://leetcode-cn.com/problems/rotate-array/
"""
#!/usr/bin/python3
#-*-coding:utf-8-*-

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        new_nums = [[] for _ in range(len_nums)]        
        for i in range(len_nums):
            new_nums[(i+k)%len_nums] = nums[i]
        for index, val in enumerate(new_nums):
           nums[index] = val

    def rotate2(self, nums: List[int], k: int) -> None:
        # 数组翻转
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        pos = k%len_nums
        nums = list(reversed(nums))   
        nums[0:pos] = reversed(nums[0:pos])
        nums[pos:len_nums] = reversed(nums[pos:len_nums])
        print(nums)

    def rotate3(self, nums: List[int], k: int) -> None:
        # 数组翻转
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1

        len_nums = len(nums)
        pos = k%len_nums
        reverse(nums, 0, len_nums-1)
        reverse(nums, 0, pos-1)
        reverse(nums, pos, len_nums-1)
        print(nums)



if __name__ == "__main__":
    num = Solution()
    num.rotate3([1,2,3,4,5,6,7],3)
