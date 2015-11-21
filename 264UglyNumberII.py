__author__ = 'yuxiangZhang'
class Solution(object):
    def nthUglyNumber(self, n):
        uglynum=[1]
        dic= {1:1}
        i2 = 0
        i3 = 0
        i5 = 0
        i = 1
        while i<n:
            u2, u3, u5 =uglynum[i2]*2,uglynum[i3]*3,uglynum[i5]*5
            if u2<=u3 and u2<=u5:
                if dic.get(u2)!=None:
                    pass
                else:
                    dic[u2]=1
                    uglynum.append(u2)
                i2 = i2 + 1
            if u3<=u2 and u3<=u5:
                if dic.get(u3)!=None:
                    pass
                else:
                    dic[u3]=1
                    uglynum.append(u3)
                i3 = i3 + 1
            if u5<=u2 and u5<=u3:
                if dic.get(u5)!=None:
                    pass
                else:
                    dic[u5]=1
                    uglynum.append(u5)
                i5 = i5 + 1
            i = i + 1
        print(uglynum)
        return uglynum[-1]
x = Solution()
print(x.nthUglyNumber(7))
