__author__ = 'yuxiangZhang'
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        area = (C-A)*(D-B) + (G-E)*(H-F)
        x1=max([A,E])
        y1=max([B,F])
        x2=min([C,G])
        y2=min([D,H])
        print(x1,y1)
        print(x2,y2)
        if x2>x1 and y2>y1:
            return area - (x2 - x1)*(y2 - y1)
        else:
            return area
x = Solution()
print(x.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))