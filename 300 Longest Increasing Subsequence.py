__author__ = 'yuxiangZhang'
class Solution(object):
    def lengthOfLIS(self, nums):
        l = len(nums)
        if l <= 1:
            return l
        ans = [1]
        for i in range(1,l):
            frontMax = 0
            for j in range(0,i):
                if nums[i] > nums[j] and ans[j] > frontMax:
                    frontMax = ans[j]
            ans.append(frontMax + 1)
        return max(ans)
