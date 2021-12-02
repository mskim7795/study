import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def bfs():
    while True:
        if len(que) == 0:
            return
        else:
            tmp = que.popleft()
            x = tmp[0]
            y = tmp[1]
            for idx in range(8):
                xx = x + dx[idx]
                yy = y + dy[idx]
                if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
                    board[xx][yy] = 0
                    que.append((xx, yy))


if __name__ == "__main__":
    n = int(input())
    board = list(list(map(int, input().split())) for _ in range(n))

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    que = deque(list())
    cnt = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                que.append((i, j))
                cnt += 1
                board[i][j] = 0
                bfs()
print(cnt)