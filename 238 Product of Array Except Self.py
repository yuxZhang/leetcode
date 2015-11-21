__author__ = 'yuxiangZhang'
class Solution(object):
    def productExceptSelf(self, nums):
        result = []
        temp = []
        l = len(nums)
        i = 0
        for i in range(l):
            result.append(1)
            temp.append(1)
        for i in range(1,l):
            print("l=",l)
            print("i=",i)
            print("l-i-1=",l-i-1)
            result[i] = result[i-1] * nums[i-1]
            temp[l-i-1] = temp[l-i] * nums[l-i]
        i = 0
        for i in range(l):
            result[i] = result[i] * temp[i]
        return result
x = Solution()
a = [1,2,4,6]
print(x.productExceptSelf(a))