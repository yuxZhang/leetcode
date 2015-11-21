__author__ = 'yuxiangZhang'
class Solution(object):
    def isUgly(self, num):
        if num<=0:
            return False
        while True:
            if num%5==0:
                num = num/5
            elif num%3==0:
                num = num/3
            elif num%2==0:
                num = num/2
            else:
                break
        if num>1:
            return False
        return True