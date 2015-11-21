# -*- coding:utf-8 -*-
__author__ = 'yuxiangZhang'

class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.temp = root
        while self.temp!= None:
            self.stack.append(self.temp)
            self.temp = self.temp.left

    def hasNext(self):
        if len(self.stack)!= 0:
            return True
        else:
            return False


    def next(self):
        temp = self.stack[-1]
        self.stack.pop(-1)
        temp2= temp.right
        while temp2!= None:
            self.stack.append(temp2)
            temp2 = temp2.left
        return temp.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
