import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def bfs(root):
    queue.append(root)
    while True:
        tmp = queue.popleft()
        if tmp == e:
            print(arr[tmp])
            return
        if arr[tmp + 1] == 0 and tmp + 1 > 0:
            queue.append(tmp + 1)
            arr[tmp + 1] = arr[tmp] + 1
        if arr[tmp - 1] == 0 and tmp - 1 > 0:
            queue.append(tmp - 1)
            arr[tmp - 1] = arr[tmp] + 1
        if arr[tmp + 5] == 0 and tmp + 5 > 0:
            queue.append(tmp + 5)
            arr[tmp + 5] = arr[tmp] + 1

if __name__ == "__main__":
    s, e = map(int, input().split())
    queue = deque(list())
    arr = [0] * 10001
    bfs(s)


