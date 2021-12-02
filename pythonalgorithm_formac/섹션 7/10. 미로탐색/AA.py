import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def dfs(coo):
    global cnt
    if coo == (6, 6):
        cnt += 1
        return
    else:
        for i in range(4):
            tmpX = coo[0] + dx[i]
            tmpY = coo[1] + dy[i]
            if 0 <= tmpX <= 6 and 0 <= tmpY <= 6 and arr[tmpX][tmpY] == 0:
                arr[tmpX][tmpY] = 1
                dfs((tmpX, tmpY))
                arr[tmpX][tmpY] = 0


if __name__ == "__main__":

    arr = list(list(map(int, input().split())) for _ in range(7))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    arr[0][0] = 1
    dfs((0, 0))

    print(cnt)