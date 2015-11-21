#-*- coding:utf-8 -*-
__author__ = 'yuxiangZhang'
class Solution(object):
    def threeSum(self, nums):
        k = int(0)
        l = len(nums)
        ans = []
        #数组先排序，nlog(n)复杂度
        nums.sort()
        #第一个数k,从小往大, n^2复杂度
        for k in range(l-2):
            #最小都比0大，那就不找了
            if nums[k] + nums[k+1] + nums[k+2] > 0:
                break
            #最大都比0小，直接找下一个吧
            if nums[k] + nums[l-2] + nums[l-1] < 0:
                continue
            print(k)
            #第二个数i从前往后扫 第三个数j从后往前扫
            i = k + 1
            j = l - 1
            while i < j:
                #sum等于0，符合加和条件
                if nums[i] + nums[j] == -nums[k]:
                    #判断这个答案之前出现过没有
                    flag = 0
                    for temp in ans:
                        if temp[0] == nums[k] and temp[1] == nums[i] and temp[2] == nums[j]:
                            flag = 1
                            break
                    #没重复就加进去
                    if flag == 0:
                        ans.append([nums[k],nums[i],nums[j]])
                    i = i + 1
                    j = j - 1
                #sum比0大,所以要变小
                elif nums[i] + nums[j] +nums[k] > 0:
                    j = j - 1
                #sum比0小，所以要变大
                else:
                    i = i + 1
        return ans
x = Solution()
nums =[3,0,-2,-1,1,2]
print(x.threeSum(nums))