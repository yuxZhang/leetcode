__author__ = 'yuxiangZhang'
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        move = [-1,0,1]
        m = len(board)
        n = 0
        if m != 0:
            n = len(board[0])
        if m == 0 or n == 0:
            return
        for i in range(0,m):
            for j in range(0,n):
                neighbor = 0
                for a in move:
                    for b in move:
                        if a == 0 and b == 0:
                            pass
                        else:
                            if i + a in range(0,m) and j + b in range(0,n):
                                if board[i+a][j+b] >= 1:
                                    neighbor = neighbor + 1
                print(neighbor)
                if neighbor <= 1 and board[i][j] == 1:
                    board[i][j] = 2
                elif (neighbor == 2 or neighbor == 3) and board[i][j] == 1:
                    pass
                elif neighbor > 3 and board[i][j] == 1:
                    board[i][j] = 2
                elif neighbor == 3 and board[i][j] == 0:
                    board[i][j] = -1
        for i in range(0,m):
            for j in range(0,n):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == -1:
                    board[i][j] = 1
        return
x = Solution()
board = [[]]
print(x.gameOfLife(board))