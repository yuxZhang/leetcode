__author__ = 'yuxiangZhang'
class Solution(object):
    def hammingWeight(self, n):
        m = 0
        sum = 0
        while n != 0:
            m = int(n / 2)
            sum = sum + n % 2
            n = m
        return sum
ans = Solution()
print(ans.hammingWeight(11))

