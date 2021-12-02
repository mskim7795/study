import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def dfs(lev, srt):
    global res
    if lev == m:
        sumV = 0
        for x in hs:
            minV = 2147000000
            for y in cb:
                minV = min(minV, abs(x[0] - pz[y][0]) + abs(x[1] - pz[y][1]))
            sumV += minV
        res = min(res, sumV)
    else:
        for i in range(srt, len(pz)):
            cb[lev] = i
            dfs(lev + 1, i + 1)
            cb[lev] = 0


if __name__ == "__main__":

    n, m = map(int, input().split())

    board = list(list(map(int, input().split())) for _ in range(n))
    hs = []
    pz = []
    cb = [0] * m
    res = 2147000000

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))

    dfs(0, 0)

    print(res)