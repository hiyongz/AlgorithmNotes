#!/usr/bin/python3
#-*-coding:utf-8-*-

# https://www.cnblogs.com/dongyangblog/p/11210820.html

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get(self):
        return self.val

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

class BinaryTreeTraversal:
    def __init__(self):
        pass


    def preorderTraversal(self,root, traverse_path=[]):
        # 前序遍历
        if root == None:
            return traverse_path
        traverse_path.append(root.data)
        self.preorderTraversal(root.left, traverse_path)
        self.preorderTraversal(root.right, traverse_path)
        return traverse_path

    def intermediateTraversal(self,root, traverse_path=[]):
        # 中序遍历
        if root == None:
            return traverse_path
        self.intermediateTraversal(root.left, traverse_path)
        traverse_path.append(root.data)
        self.intermediateTraversal(root.right, traverse_path)
        return traverse_path

    def postorderTraversal(self,root, traverse_path=[]):
        # 后序遍历
        if root == None:
            return
        self.postorderTraversal(root.left, traverse_path)
        self.postorderTraversal(root.right, traverse_path)
        traverse_path.append(root.data)
        return traverse_path

if __name__ == "__main__":
    bintree = BinaryTree('A')
    bintree.setLeft(BinaryTree('B'))
    bintree.setRight(BinaryTree('C'))
    bintree.getLeft().setLeft(BinaryTree('D'))
    bintree.getLeft().getLeft().setRight(BinaryTree('G'))

    bintree.getRight().setRight(BinaryTree('F'))
    bintree.getRight().setLeft(BinaryTree('E'))

    bintree.getRight().getRight().setLeft(BinaryTree('H'))

    Traversal = BinaryTreeTraversal()
    print(Traversal.preorderTraversal(bintree))
    print(Traversal.intermediateTraversal(bintree))
    print(Traversal.postorderTraversal(bintree))











