__author__ = 'yuxiangZhang'
class Solution(object):
    m=[]
    def searchMatrix(self, matrix, target):
        a = len(matrix)
        b = len(matrix[0])
        self.m = matrix
        return self.findnum(0,a-1,0,b-1,target)
    def findnum(self,x1,x2,y1,y2,target):
        if (x2-x1)<=1 and (y2-y1)<=1:
            if self.m[x1][y1]!=target and self.m[x1][y2]!=target and self.m[x2][y1]!=target and self.m[x2][y2]!=target:
                return False
            else:
                return True
        x, y= int((x2 + x1)/2),int((y1 + y2)/2)
        if self.m[x][y] == target:
            return True
        elif self.m[x][y]>target:
            return (self.findnum(x1,x,y1,y,target) or self.findnum(x1,x,y,y2,target) or self.findnum(x,x2,y1,y,target))
        else:
            return (self.findnum(x,x2,y1,y,target) or self.findnum(x,x2,y,y2,target) or self.findnum(x1,x,y,y2,target))
x = Solution()
k = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

print(x.searchMatrix(k,5))
