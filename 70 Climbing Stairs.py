__author__ = 'yuxiangZhang'
class Solution(object):
    def climbStairs(self, n):
        ans = [0,1,2]
        if n <= 2:
            return ans[n]
        i = 3
        while i <= n:
            ans.append(ans[i-1] + ans[i-2])
            i = i + 1
        return ans[n]