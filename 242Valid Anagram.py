__author__ = 'yuxiangZhang'
class Solution(object):
    def isAnagram(self, s, t):
        ds = dict()
        dt = dict()
        if len(s) != len(t):
            return False
        for i in s:
            if ds.get(i) == None:
                ds[i] = 1
            else:
                ds[i] = ds[i] + 1
        for i in t:
            if dt.get(i) == None:
                dt[i] = 1
            else:
                dt[i] = dt[i] + 1
        if len(s)!=len(t):
            return False
        for n in ds:
            if dt.get(n) == None:
                return False
            elif dt[n]!=ds[n]:
                return False
        return True
x = Solution()
a = 'baha'
b = 'aahh'
print(x.isAnagram(a,b))