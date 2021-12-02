import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


if __name__ == "__main__":
    m, n = map(int, input().split())
    board = list(list(map(int, input().split())) for _ in range(n))
    que = deque()
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                que.append((i, j, 0))
    while True:

        if len(que) == 0:
            break
        else:
            tmp = que.popleft()
            for i in range(4):
                x = tmp[0] + dx[i]
                y = tmp[1] + dy[i]
                res = tmp[2]
                if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
                    board[x][y] = 1
                    que.append((x, y, tmp[2] + 1))

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                res = -1
    print(res)