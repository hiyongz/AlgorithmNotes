#!/usr/bin/python3
#-*-coding:utf-8-*-

# 106. 从中序与后序遍历序列构造二叉树:https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        n = len(inorder)
        # 将inorder保存为字典
        index = {element: i for i, element in enumerate(inorder)}


        def mybuildTree(inorder_left: int, inorder_right: int):
            if inorder_left > inorder_right or len(postorder)==0:
                return None
            # 找到根节点
            # 后序遍历中的最后一个节点是根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 在中序遍历中定位根节点位置
            inorder_root = index[val]
            root.left = mybuildTree(inorder_left, inorder_root-1)
            # 右子树
            root.right = mybuildTree(inorder_root+1, inorder_right)
            # 左子树
            # root.left = mybuildTree(inorder_left, inorder_root-1)        
            return root
        return mybuildTree(0, n - 1)


    def postorderTraversal(self,root, traverse_path=[]):
        # 后序遍历
        if root == None:
            return
        self.postorderTraversal(root.left, traverse_path)
        self.postorderTraversal(root.right, traverse_path)
        traverse_path.append(root.val)
        return traverse_path

if __name__ == "__main__":
    solu = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    result = solu.buildTree(inorder,postorder)
    traverse_path = solu.postorderTraversal(result)
    print(traverse_path)