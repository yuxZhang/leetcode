# -*- coding:utf-8 -*-
__author__ = 'yuxiangZhang'
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        if len(nums) == 4:
            return max(nums[0]+nums[2], nums[1]+nums[3])
        # There are two 3 situations. the first pick  is 1 or 2 or 3.
        # Situation 1:
        temp1 = int(0)
        c1   = int(0)
        m1   = int(0)
        for i in range(2,len(nums)):
            temp1 = max(c1, m1)
            c1    = m1 + nums[i]
            m1    = temp1
        max1=max(c1-nums[len(nums)-1]+nums[0],m1+nums[0])
        #Situation 2:
        temp2 = int(0)
        c2   = int(0)
        m2   = int(0)
        for i in range(3,len(nums)):
            temp2 = max(c2, m2)
            c2    = m2 + nums[i]
            m2    = temp2
        max2 = max(c2+nums[1],m2+nums[1])
        #Situation 3:
        temp3 = int(0)
        c3   = int(0)
        m3   = int(0)
        for i in range(4,len(nums)):
            temp3 = max(c3, m3)
            c3    = m3 + nums[i]
            m3    = temp3
        max3 = max(c3+nums[2],m3+nums[2])
        return max(max1, max2, max3)