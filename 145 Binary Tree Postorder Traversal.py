__author__ = 'yuxiangZhang'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def postorderTraversal(self, root):
        stack = []
        ans = []
        if root == None:
            return ans
        stack.append(root)
        while len(stack)!=0:
            l = len(stack) - 1
            if stack[l].left == None and stack[l].right == None:
                ans.append(stack[l].val)
                stack.pap()
            if stack[l].right != None:
                stack.append(stack[l].right)
                stack[l].right = None
            if stack[l].left != None:
                stack.append(stack[l].left)
                stack[l].left = None
        return ans