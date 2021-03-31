#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
11. 盛最多水的容器
https://leetcode-cn.com/problems/container-with-most-water/
"""
class Solution:
    def maxArea(self, height: List[int]):
        l, r = 0, len(height)-1

        max_area = 0
        while l < r:
            area = min(height[l],heught(r) * (r-l)
            max_area = max(max_area,area)

            if height[l] < height[r]:
                l = l + 1
            else:
                r -= 1
        return max_area

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.maxArea([1,8,6,2,5,4,8,3,7])
    print(result)