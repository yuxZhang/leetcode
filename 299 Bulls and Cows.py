__author__ = 'yuxiangZhang'
class Solution(object):
    def getHint(self, secret, guess):
        dic = dict()
        l = len(secret)
        i = 0
        A = int(0)
        secret = list(secret)
        guess = list(guess)
        B = int(0)
        while i < l:
            if secret[i] == guess[i]:
                secret.pop(i)
                guess.pop(i)
                A = A + 1
                l = l - 1
            else:
                if secret[i] in dic:
                    dic[secret[i]] = dic[secret[i]] + 1
                else:
                    dic[secret[i]] = 1
                i = i + 1
        for i in guess:
            if i in dic and dic[i] >= 1:
                B = B + 1
                dic[i] = dic[i] - 1

        return str(A) + "A" + str(B) + "B"





