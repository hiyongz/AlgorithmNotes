#!/usr/bin/python3
#-*-coding:utf-8-*-

# https://www.cnblogs.com/dongyangblog/p/11210820.html

class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeTraversal:
    def preorder(self,root, traverse_path=[]):
        # 前序遍历
        if root == None:
            return traverse_path
        traverse_path.append(root.val)
        self.preorder(root.left, traverse_path)
        self.preorder(root.right, traverse_path)
        return traverse_path

    def inorder(self,root, traverse_path=[]):
        # 中序遍历
        if root == None:
            return traverse_path
        self.inorder(root.left, traverse_path)
        traverse_path.append(root.val)
        self.inorder(root.right, traverse_path)
        return traverse_path

    def postorder(self,root, traverse_path=[]):
        # 后序遍历
        if root == None:
            return
        self.postorder(root.left, traverse_path)
        self.postorder(root.right, traverse_path)
        traverse_path.append(root.val)
        return traverse_path

if __name__ == "__main__":
    root = BinaryTree('A')
    root.left = BinaryTree('B')
    root.right = BinaryTree('C')
    root.left.left  = BinaryTree('D')
    root.left.left.right  = BinaryTree('G')
    root.right.left = BinaryTree('E')
    root.right.right = BinaryTree('F')
    root.right.right.left = BinaryTree('H')

    Traversal = BinaryTreeTraversal()
    print(Traversal.preorder(root))
    print(Traversal.inorder(root))
    print(Traversal.postorder(root))











