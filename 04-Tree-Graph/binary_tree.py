#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/12 19:08
# @Author:  haiyong
# @File:    binary_tree.py

import math
from asyncio.windows_events import NULL
from idlelib.tree import TreeNode

a = 16
print(math.log(a, 10)/math.log(2,10))
print(math.log(2,10))

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left) + 1
            right_depth = self.maxDepth(root.right) + 1
            return max(left_depth, right_depth)

max_depth = Solution()
max_depth.maxDepth([3,9,20,NULL,NULL,15,7])