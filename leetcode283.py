__author__ = 'yuxiangZhang'
'''class Solution(object):
    def moveZeroes(self, nums):

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        '''
nums = [0,0 , 1]
i = 0
while i <= len(nums) - 1:
    if nums[i] == 0:
        flag = 0
        j = i + 1
        while j<= len(nums) - 1:
            if nums[j] != 0:
                flag = 1
                break
            j = j + 1
        if flag == 1:
            nums.pop(i)
            nums.append(0)
        else:
            i = i + 1
            break
    else:
        i = i + 1
for i in nums:
    print(i)