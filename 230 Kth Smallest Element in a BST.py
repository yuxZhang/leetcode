__author__ = 'yuxiangZhang'
class Solution(object):
    cur = int(1)
    ans = int()
    def kthSmallest(self, root, k):
        self.cur = 0
        self.findnum(root,k)
        return self.ans 
    def findnum(self,node,k):
        if node.left != None:
            self.findnum(node.left,k)
        self.cur = self.cur + 1
        if self.cur == k:
            self.ans = node.val
        if node.right != None:
            self.findnum(node.right,k)
        