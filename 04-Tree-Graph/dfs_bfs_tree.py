#!/usr/bin/python3
#-*-coding:utf-8-*-

from typing import List

# 二叉树DFS、BFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def DFSTrav(self, node, visited): 
        # 标记已经访问过的节点
        if node.val in visited:
            return
        
        visited.append(node.val)
 
        # 访问当前节点的相邻节点
        if node.left:
            self.DFSTrav(node.left, visited)
        if node.right:
            self.DFSTrav(node.right, visited)


    def dfs(self, root: TreeNode) -> List[List[int]]:
        visited = []
        # dfs
        self.DFSTrav(root, visited)
        print(visited)

    def dfs2(self, node): 
        visited = []
        stack = []
        stack.append(node)
        visited.append(node.val)
        while stack:
            if not node.left and not node.right:
                stack.pop()
            node = stack[-1]

            if node.left and node.left.val not in visited:                
                stack.append(node.left)
                visited.append(node.left.val)
                node = node.left

            elif node.right and node.right.val not in visited:
                stack.append(node.right)
                visited.append(node.right.val)
                node = node.right
            else:
                stack.pop()
        print(visited)

    def bfs(self, root: TreeNode) -> List[List[int]]:
        visited = []
        if not root:
            return visited
                
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                node = queue.pop(0)
                # 存储当前节点
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            visited.append(level)
        print(visited)
        return visited



if __name__ == "__main__":
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left  = TreeNode('D')
    root.left.left.right  = TreeNode('G')
    root.right.left = TreeNode('E')
    root.right.right = TreeNode('F')
    root.right.right.left = TreeNode('H')
    
    solu = Solution()
    solu.dfs(root)
    solu.dfs2(root)
    solu.bfs(root)
    # print(visited)




