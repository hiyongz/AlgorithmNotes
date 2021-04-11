#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
70. 爬楼梯
https://leetcode-cn.com/problems/climbing-stairs/
"""

# f(1)：1
# f(2)：2
# f(3)：f(1) + f(2)
# f(4): f(2) + f(3)

class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2, s3 = 1,2,3
        if n <= 2:
            return n
        for _ in range(3,n+1):
            s3 = s1 + s2
            s1 = s2
            s2 = s3
        return s3

if __name__ == "__main__":
    Solu = Solution()
    result = Solu.climbStairs(3)
    print(result)



