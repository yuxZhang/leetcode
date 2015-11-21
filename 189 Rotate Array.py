# -*- coding=utf-8 -*-
__author__ = 'yuxiangZhang'
class Solution(object):
    def rotate(self, nums, k):
        temp = nums[-1]
        while k>0:
            temp = nums[-1]
            nums.insert(0, temp)
            nums.pop(-1)
            k = k - 1


