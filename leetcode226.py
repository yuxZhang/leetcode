__author__ = 'yuxiangZhang'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        else:
            root.right ,root.left = root.left ,root.right
            self.invertTree(root.right)
            self.invertTree(root.left)

