__author__ = 'yuxiangZhang'
class Solution(object):
    def wordPattern(self, pattern, str):
        count = int(0)
        i = int(0)
        str = str+' '
        for i in range(len(str)):
            if str[i] == ' ':
                count = count + 1
        if len(pattern)!=(count):
            return False
        dic = dict()
        j = 0
        i = 0
        strtemp = []
        while j<len(str):
            if str[j+1] == ' ':
                strtemp.append(str[i:j+1])
                i = j + 2
                j = j + 2
            else:
                j = j + 1
        i = 0
        for i in range(len(pattern)):
            if (pattern[i] in dic)==True:
                if dic.get(pattern[i])!=strtemp[i]:
                    return False
            else:
                for temp in dic:
                    if dic.get(temp) == strtemp[i]:
                        return False
                dic[pattern[i]]=strtemp[i]
        return True
a = 'aabb'
b = 'dog dog boy boy'
x = Solution()
print(x.wordPattern(a,b))


