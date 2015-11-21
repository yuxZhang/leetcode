__author__ = 'yuxiangZhang'
class Solution(object):
    def fourSum(self, nums, target):
        k = int(0)
        l = len(nums)
        ans = []
        nums.sort()
        print(nums)
        for k1 in range(l-3):
            if nums[k1] + nums[k1+1] + nums[k1+2] + nums[k1+3] > target:
                break
            elif nums[k1] + nums[l-3] + nums[l-2] + nums[l-1] < target:
                continue
            for k2 in range(k1+1 ,l-2):
                if nums[k1] + nums[k2] + nums[k2+1] + nums[k2+2] > target:
                    break
                elif nums[k1] + nums[k2] + nums[l-2] + nums[l-1] < target:
                    continue
                i = k2 + 1
                j = l - 1
                while i < j:
                    if nums[i] + nums[j] == target -(nums[k1] + nums[k2]):
                        flag = 0
                        for temp in ans:
                            if temp[0] == nums[k1] and temp[1]== nums[k2] and temp[2] == nums[i] and temp[3] == nums[j]:
                                flag = 1
                                break
                        if flag == 0:
                            ans.append([nums[k1], nums[k2], nums[i], nums[j]])
                        i = i + 1
                        j = j - 1
                    elif nums[i] + nums[j] > target - (nums[k1] + nums[k2]):
                        j = j - 1
                    else:
                        i = i + 1
        return ans
x = Solution()
nums =[3,0,-2,-1,1,2]
print(x.fourSum(nums, 0))

