#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/11 19:58
# @Author:  haiyong
# @File:    preorder.py
# N叉树简洁递归
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res

# N叉树通用递归模板
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res

