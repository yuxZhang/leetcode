__author__ = 'yuxiangZhang'
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    a = [0,0,1,1]
    if a[version]==1:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1)==True:
            return 1
        return int(self.halffind(1,n))
    def halffind(self,start,end):
        if end==(start+1):
            return end
        if isBadVersion(int((start+end)/2))==True:
            print(start,(start+end)/2)
            return self.halffind(start,(start+end)/2)
        else:
            return self.halffind((start+end)/2,end)

x = Solution()
print(x.firstBadVersion(3))