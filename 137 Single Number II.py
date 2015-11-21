__author__ = 'yuxiangZhang'
class Solution(object):
    def singleNumber(self, nums):
        cur = 30                  # manipulating the No.(cur+1) bit (from 30 to 0)
        ans = 0
        sign = 0                  # the sign bit
        for i in nums:
            if i < 0:
                sign = sign + 1
        if sign%3 == 1:
            sign = 1
        else:
            sign = 0              #"1" is nagetive "0" is positive
        print("sign=",sign)
        while cur >= 0:
            s = 0                 # s is the sum of all the No.cur bits
            i = 0
            for i in range(len(nums)):
                temp = nums[i]
                temp = temp >> cur
                temp = temp & 1
                s = s + temp
            ans = ans << 1
            if s%3 == 1 :
                ans = ans | 1
            cur = cur - 1
        if sign == 1:
            ans = -((1<<31)-ans)   #when ans is nagetive
        return ans
x = Solution()
a = [-3,-3,-4,-3]
print(x.singleNumber(a))
