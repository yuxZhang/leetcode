# -*- coding:utf-8 -*-
__author__ = 'yuxiangZhang'
# 递推公式的意义 第 i 个如果选了 则chosen = num[i] + missed (即i-1 没入选的情况)
#                如果第 i 没被选择  则missed = (第i-1被选或没被选的中的大的值 因为无所谓）
class Solution(object):
    def rob(self, nums):
        chosen = int(0)
        missed = int(0)
        temp   = int(0)
        for i in range(len(nums)):
            temp = max(chosen, missed)
            chosen = missed + nums[i]
            missed = temp
        return max(chosen, missed)
