__author__ = 'yuxiangZhang'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif (p != None and q == None) or (p == None and q != None):
            return False
        elif p.var != q.var:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
