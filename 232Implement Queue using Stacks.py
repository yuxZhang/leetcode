__author__ = 'yuxiangZhang'
class Queue(object):
    def __init__(self):
        self.stack = []


    def push(self, x):
        self.stack.append(x)


    def pop(self):
        self.stack.pop(0)

    def peek(self):
        return self.stack[0]


    def empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
