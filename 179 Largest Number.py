__author__ = 'yuxiangZhang'
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        l = len(nums)
        for i in range(0, l-1):
            for j in range(0, l-i-1):
                if self.compare(nums[j], nums[j+1])<0:
                    nums[j], nums[j+1] =nums[j+1], nums[j]
        strtemp=""
        for i in range(0, l):
            strtemp = strtemp + str(nums[i])
        if strtemp[0] == '0':
            strtemp='0'
        return strtemp

    def compare(self,n1,n2):
        str1 = str(n1) + str(n2)
        str2 = str(n2) + str(n1)
        for i in range(len(str1)):
            if str1[i] > str2[i]:
                return 1
            elif str1[i] < str2[i]:
                return -1
        return 0
