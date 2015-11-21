# -*- coding:utf-8 -*-
__author__ = 'yuxiangZhang'
class Solution(object):
    def reverseBits(self, n):
        temp = bin(n)
        print(bin(n))
        strtemp = list(str(temp))
        strtemp.reverse()
        strtemp.pop(-1)
        strtemp.pop(-1)
        while len(strtemp)!=32:
            strtemp.append('0')
        print(strtemp)
        strtemp = "".join(strtemp)
        return int(strtemp, base=2)

x = Solution()
print(x.reverseBits(43261596))

