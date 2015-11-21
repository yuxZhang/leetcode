__author__ = 'yuxiangZhang'
class Solution(object):
    def summaryRanges(self, nums):
        ans = []
        start = 0
        end = 0
        l = len(nums)
        i = 0
        while start < l:
            i = start
            while (i + 1) != l and (nums[i] + 1) == nums[i+1]:
                i = i + 1
            end = i
            if start == end:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start])+"->"+str(nums[end]))
            if (i + 1) == l:
                break;
            else:
                start = i +1
        return ans
