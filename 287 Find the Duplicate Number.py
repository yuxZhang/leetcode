__author__ = 'yuxiangZhang'
class Solution(object):
    def findDuplicate(self, nums):
        start = int(1)
        end = int(len(nums)-1)
        count = int(0)
        mid = int(0)
        while start<end:
            mid = int((start+end)/2)
            count = 0
            for i in nums:
                if i<=mid:
                    count += 1
            if count > mid:
                end =  mid
            else:
                start = mid + 1
        return end
x = Solution()
print(x.findDuplicate([3, 3, 1, 4 ,2]))