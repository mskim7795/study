import sys
from collections import deque
# sys.stdin = open("input.txt", "r")



if __name__ == "__main__":
    n = int(input())
    board = list(list(map(int, input().split())) for _ in range(n))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    maxV = 0


    for i in range(1, 101):
        rain = i
        cnt = 0
        ch = list([0] * n for _ in range(n))

        for j in range(n):
            for k in range(n):
                if ch[j][k] == 0 and board[j][k] > rain:
                    ch[j][k] = 1
                    que = deque()
                    que.append((j, k))
                    while True:
                        if len(que) == 0:
                            break
                        else:
                            tmp = que.popleft()
                            x = tmp[0]
                            y = tmp[1]
                            for m in range(4):
                                xx = x + dx[m]
                                yy = y + dy[m]
                                if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > rain:
                                    que.append((xx, yy))
                                    ch[xx][yy] = 1
                    cnt += 1
        maxV = max(cnt, maxV)
    print(maxV)