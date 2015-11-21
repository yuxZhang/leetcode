__author__ = 'yuxiangZhang'
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        alist = []
        i = 0
        for i in range(200000):
            alist.append(0)
        while n <= len(nums) - 1:
            if nums[n] >= 0:
                alist[nums[n]] = alist[nums[n]] + 1
            else:
                alist[-nums[n]+100000] = alist[-nums[n]+100000] + 1
            n = n + 1
        i = 0
        for i in range(200000):
            if alist[i] == 1:
                if i <= 80000:
                    self = i
                    return self
                else:
                    selnf = -( i - 100000)
                    return self



alist = [2, 1, 2,4,6,6,1]
x = 0
print(singleNumber(x,alist))

