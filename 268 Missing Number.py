__author__ = 'yuxiangZhang'
class Solution(object):
    def missingNumber(self, nums):
        return  int(float((len(nums)+1))/2*len(nums)-sum(nums))
a = [0 , 1]
x = Solution()
print(x.missingNumber(a))