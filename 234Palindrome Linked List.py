__author__ = 'yuxiangZhang'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def isPalindrome(self, head):
        #find the middle of the list
        fast = head
        slow = head
        if head==None:    #len=0
            return True
        if head.next==None:   #len=1
            return True
        if head.next.next==None:
            if head.val==head.next.val:
                return True
            else:
                return False
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        p = ListNode(0)
        q = ListNode(0)
        temp =  p
        temp1 = p
        if fast.next!=None:
            q = slow.next.next
            p = slow.next
            slow.next = None
        else:
            p = slow.next
            q = p.next
            p.next = None
            slow.next = None
        while q!=None:
            temp = q
            temp1 = p
            p = temp
            q = q.next
            p.next = temp1
        while p!=None and head!=None:
            if p.val!=head.val:
                return False
            p = p.next
            head = head.next
        return True

l=[1,2,1]
h = ListNode(0)
p = ListNode(0)
h.next = p
for i in range(len(l)):
    temp = ListNode(l[i])
    p.next = temp
    p = p.next
h = h.next.next
x=Solution()
print("h.val=",h.val)
print("h.next.val=",h.next.val)
print(x.isPalindrome(h))