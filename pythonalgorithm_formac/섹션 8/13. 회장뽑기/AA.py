import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n = int(input())
    arr = list([n] * (n + 1) for _ in range(n + 1))
    dp = [0] * (n + 1)
    minV = 2147000000
    res = []
    while True:
        s, e = map(int, input().split())
        if s == e == -1:
            break
        else:
            arr[s][e] = 1
            arr[e][s] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if arr[i][k] != n and arr[k][j] != n:
                    arr[i][j] = arr[j][i] = min(arr[i][j], arr[i][k] + arr[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] != n:
                dp[i] = max(dp[i], arr[i][j])

        minV = min(minV, dp[i])
    cnt = 0
    for i in range(1, n + 1):
        if dp[i] == minV:
            cnt += 1
            res.append(i)
    print(minV, cnt)
    for x in res:
        print(x, end=" ")
