class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return root
        elif self.ifCommonAncestor(root,p,q) == True and self.ifCommonAncestor(root.right,p,q) == False and self.ifCommonAncestor(root.left,p,q) == False:
            return root
        elif self.ifCommonAncestor(root.right,p,q) == True:
            return self.lowestCommonAncestor(root.right,p,q)
        elif self.ifCommonAncestor(root.left,p,q) == True:
            return self.lowestCommonAncestor(root.left,p,q)
    def ifCommonAncestor(self,root,p,q):
        if self.ifAncestor(root,p) and self.ifAncestor(root,q):
            return True
        else:
            return False
    def ifAncestor(self,root,p):
        if root == None:
            return False
        if root.val == p.val:
            return True
        elif root.val <  p.val:
            if root.right == None:
                return False
            else:
                return self.ifAncestor(root.right,p)
        elif root.val > p.val:
            if root.left == None:
                return False
            else:
                return self.ifAncestor(root.left,p)
n = TreeNode(2)
n.left = TreeNode(1)
x = Solution()
ans = x.lowestCommonAncestor(n,n,n.left)
print(ans.val)