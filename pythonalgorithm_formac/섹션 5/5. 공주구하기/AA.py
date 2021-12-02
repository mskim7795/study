import sys
# sys.stdin = open("input.txt", "r")
from collections import deque

n, k = map(int, input().split())

prc = list(range(1, n + 1))
prc = deque(prc)
cnt = 0
while len(prc) != 1:
    cnt += 1
    tmp = prc.popleft()
    if cnt != k:
        prc.append(tmp)
    else:
        cnt = 0
print(prc.pop())