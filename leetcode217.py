__author__ = 'yuxiangZhang'
class Solution(object):
    def containsDuplicate(self, nums):
        self.quicksort(0,len(nums)-1,nums)
        i = 0
        for i in range(0,len(nums)-2):
            if nums[i] == nums[i+1]:
                return True
        return False
    def quicksort(self,start,end,nums):
        if start >= end:
            return
        i = start
        j = end
        key = nums[i]
        while i < j:
            while i < j and nums[j] >= key:
                j = j - 1
            nums[i] = nums[j]
            while i < j and nums[i] <= key:
                i = i + 1
            nums[j] = nums[i]
        nums[j] = key
        self.quicksort(start,j-1,nums)
        self.quicksort(j+1,end,nums)
        return

