__author__ = 'yuxiangZhang'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None :
            return None
        if head.next==None:
            return head
        p, q = head, head.next
        p.next = None
        print(p.val,q.val)
        while q!=None:
            temp = q.next
            q.next = p
            p = q
            q = temp
        return p
a = ListNode(1)
b = ListNode(2)
a.next = b
x = Solution()
ans = x.reverseList(a)
print(ans.val,ans.next.val,ans.next.next)