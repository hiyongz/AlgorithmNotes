#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/9/1 20:13
# @Author:  haiyong
# @File:    inorderTraversal.py

# iteratively
from idlelib.tree import TreeNode
from typing import List

from null import Null


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
if __name__ == "__main__":
    Solu = Solution()
    result = Solu.inorderTraversal([1,1,2,3])
    print(result)