__author__ = 'yuxiangZhang'
def addDigits( num):
    print("num=",num)
    if num <= 9:
        return num
    else:
        strtemp = str(num)
        print("strtemp="+strtemp)
        i = 0
        sum = 0
        for i in range(len(strtemp)):
            sum = int(strtemp[i]) + sum
        print("sum=",sum)
        return addDigits(sum)
a = 45
p = addDigits(a)
print(p)