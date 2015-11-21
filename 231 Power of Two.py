__author__ = 'yuxiangZhang'
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        a = bin(n)
        l = len(a)
        for i in range(2,l):
            if a[i]=='1':
                if i!=2:
                    return False
        return True
x = Solution()
print(x.isPowerOfTwo(5))