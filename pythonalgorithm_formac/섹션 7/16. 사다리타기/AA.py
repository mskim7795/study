import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def dfs(x, y, direct):
    global res, tmp
    if x == 9:
        if board[x][y] == 2:
            res = tmp
    else:
        board[x][y] = 0
        if direct == 0:
            if y + 1 < 10 and board[x][y + 1] != 0:
                dfs(x, y + 1, 1)
                board[x][y + 1] = 1
            elif y - 1 >= 0 and board[x][y - 1] != 0:
                dfs(x, y - 1, -1)
                board[x][y - 1] = 1
            else:
                dfs(x + 1, y, 0)
                board[x + 1][y] = 1
        elif direct == 1:
            if board[x + 1][y] != 0 and y + 1 < 10 and board[x][y + 1] != 0:
                dfs(x, y + 1, 1)
                board[x][y + 1] = 1
            elif board[x + 1][y] != 0:
                dfs(x + 1, y, 0)
                board[x + 1][y] = 1
            else:
                dfs(x, y + 1, 1)
                board[x][y + 1] = 1
        else:
            if board[x + 1][y] != 0 and y - 1 >= 0 and board[x][y - 1] != 0:
                dfs(x, y - 1, -1)
                board[x][y - 1] = 1
            elif board[x + 1][y] != 0:
                dfs(x + 1, y, 0)
                board[x + 1][y] = 1
            else:
                dfs(x, y - 1, -1)
                board[x][y - 1] = 1


if __name__ == "__main__":
    board = list(list(map(int, input().split())) for _ in range(10))

    dx = [-1, 1, 0 ,0]
    dy = [0, 0, 1, -1]
    res = -1
    for i in range(10):
        if board[0][i] == 1:
            tmp = i
            dfs(0, i, 0)
            board[0][i] = 1


    print(res)