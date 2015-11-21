__author__ = 'yuxiangZhang'
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) == 0 or k <= 0 or t < 0:
            return False
        dic = dict()
        t = t + 1
        for index , value in enumerate(nums):
            n = value / t
            if n in dic:
                if abs(dic[n][0] - index) <= k:
                    return True
            if n - 1 in dic:
                if abs(dic[n-1][0] - index) <= k and abs(dic[n-1][1] - value) < t:
                    return True
            if n + 1 in dic:
                if abs(dic[n+1][0] - index) <= k and abs(dic[n+1][1] - value) < t:
                    return True
            x = [index,value]
            dic[n] = x
        return False