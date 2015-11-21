__author__ = 'yuxiangZhang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ans = []
    def binaryTreePaths(self, root):
        a = []
        if root == None:
            return a
        self.findpath(root,a)
        print("len=",len(self.ans))
        return self.ans
    def findpath(self,node,path):
        pathnew=path
        if len(pathnew)==0:
            pathnew = str(node.val)
        else:
            pathnew = pathnew + '->' + str(node.val)
        if node.left == None and node.right == None:
            if pathnew=='1':
                print("caonima")
            self.ans.append(pathnew)
        if node.left!=None:
            self.findpath(node.left,pathnew)
        if node.right!=None:
            self.findpath(node.right,pathnew)
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
a.left = b
b.right = d
a.right = c
x = Solution()
print(x.binaryTreePaths(a))