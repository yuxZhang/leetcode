# -*- coding:utf-8 -*-
__author__ = 'yuxiangZhang'
class Solution(object):
    def isHappy(self, n):
        if n<=0:
            return False
        r1 = self.getSum(n)
        r2 = self.getSum(self.getSum(n))
        while True:
            if r1 == 1:
                return True
            if r1 == r2:
                return False
            r1 = self.getSum(r1)
            r2 = self.getSum(self.getSum(r2))
    def getSum(self, m):
        n = m
        s = 0
        while n>0:
            s = s + (n%10)*(n%10)
            n = n // 10
        return s

