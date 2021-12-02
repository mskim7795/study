import sys
# sys.stdin = open("input.txt", "r")
from collections import deque

n, m = map(int, input().split())
pai = list(map(int, input().split()))
pai = deque(pai)
cnt = 0
while True:
    maxV = max(pai)
    tmp = pai.popleft()

    if tmp == maxV:
        cnt += 1
        if m == 0:
            break
        else:
            if m == 0:
                m = len(pai) - 1
            else:
                m -= 1
    else:
        pai.append(tmp)
        if m == 0:
            m = len(pai) - 1
        else:
            m -= 1

print(cnt)

