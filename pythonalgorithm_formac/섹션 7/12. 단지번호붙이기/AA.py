import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def bfs():
    num = 0
    while True:
        if len(que) == 0:
            return num
        else:
            tmp = que.popleft()
            x = tmp[0]
            y = tmp[1]

            num += 1
            for i in range(4):
                tmpX = x + dx[i]
                tmpY = y + dy[i]
                if 0 <= tmpX < n and 0 <= tmpY < n and arr[tmpX][tmpY] == 1:
                    que.append((tmpX, tmpY))
                    arr[tmpX][tmpY] = 0




if __name__ == "__main__":
    n = int(input())
    arr = list()
    for i in range(n):
        m = input()
        tmpArr = list()
        for b in m:
            tmpArr.append(int(b))
        arr.append(tmpArr)

    cnt = list()
    res = 0
    que = deque(list())
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                que.clear()
                que.append((i, j))
                arr[i][j] = 0
                cnt.append(bfs())
                res += 1
    print(res)
    cnt.sort()
    for a in cnt:
        print(a)