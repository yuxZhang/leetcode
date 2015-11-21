__author__ = 'yuxiangZhang'
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = dict()
        l = len(nums)
        for i in range(0,l):
            if nums[i] in dic:
                if (i-dic[nums[i]])<=k:
                    return True
            dic[nums[i]] = i
        return False