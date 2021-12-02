import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

cls = list(input())
n = int(input())
for i in range(n):
    ex1 = deque(list(input()))
    leng = len(cls)
    cnt = 0
    res = ""
    while ex1:
        tmp = ex1.popleft()
        if tmp == cls[cnt]:
            cnt += 1
        else:
            check = 0
            for j in range(cnt + 1, leng):
                if tmp == cls[j]:
                    check = 1
                    break
            if check == 1:
                res = "#" + str(i + 1) + " NO"
                break
        if cnt == leng:
            res = "#" + str(i + 1) + " YES"
            break
    else:
        res = "#" + str(i + 1) + " NO"
    print(res)

