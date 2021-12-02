import sys
from collections import deque
# sys.stdin = open("input.txt", "r")



arr = list(list(map(int, input().split())) for _ in range(7))

arr.insert(0, [1] * 9)
arr.insert(8, [1] * 9)
for i in range(1, 8):
    arr[i].insert(0, 1)
    arr[i].append(1)
res = 0

que = deque()
que.append([1, 1])

while True:
    if len(que) == 0:
        res = -1
        break
    else:
        tmp = que.popleft()
        x = tmp[0]
        y = tmp[1]
        if tmp == [7, 7]:
            res = arr[x][y]
            break
        x += 1

        if arr[x][y] == 0:
            que.append([x, y])
            arr[x][y] = arr[x - 1][y] + 1

        x -= 1
        y += 1
        if arr[x][y] == 0:
            que.append([x, y])
            arr[x][y] = arr[x][y - 1] + 1
        y -= 1
        x -= 1
        if arr[x][y] == 0:
            que.append([x, y])
            arr[x][y] = arr[x + 1][y] + 1
        x += 1
        y -= 1
        if arr[x][y] == 0:
            que.append([x, y])
            arr[x][y] = arr[x][y + 1] + 1
        y += 1

print(res)