__author__ = 'yuxiangZhang'
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minValue = int(0)


    def push(self, x):
        if len(self.stack) == 0:
            self.minValue = x
        else:
            if x < self.minValue:
                self.minValue = x
        self.stack.append(x)


    def pop(self):
        if self.stack[len(self.stack)-1] == self.minValue:
            self.stack.pop()
            if len(self.stack) != 0:
                self.minValue = self.stack[0]
                for i in self.stack:
                    if i < self.minValue:
                        self.minValue = i
            else:
                self.minValue = 0
        else:
            self.stack.pop()

    def top(self):
        return self.stack[len(self.stack)-1]


    def getMin(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.minValue