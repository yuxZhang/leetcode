__author__ = 'yuxiangZhang'
class Stack(object):
    def __init__(self):
        self.stack = []


    def push(self, x):
        self.stack.append(x)


    def pop(self):
        self.stack.pop()


    def top(self):
        return self.stack[-1]


    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False