import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def dfs(coo):
    global cnt
    if arr[coo[0]][coo[1]] == maxV:
        cnt += 1
        return
    else:
        for i in range(4):
            x = coo[0] + dx[i]
            y = coo[1] + dy[i]
            if 0 <= x < n and 0 <= y < n and arr[x][y] > arr[coo[0]][coo[1]]:
                dfs((x, y))


if __name__ == "__main__":
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    minV = 2147000000
    minCoo = (-1, -1)
    maxV = -2147000000
    maxCoo = (-1, -1)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] < minV:
                minV = arr[i][j]
                minCoo = (i, j)
            if arr[i][j] > maxV:
                maxV = arr[i][j]
                maxCoo = (i, j)

    dfs(minCoo)


    print(cnt)