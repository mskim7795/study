import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n, m = map(int, input().split())

    arr = list(list(map(int, input().split())) for _ in range(n))
    arr.insert(0, [0, 0])

    dp = list([0] * (m + 1) for _ in range(n + 1))

    for i in range(1, n + 1):
        for j in range(m + 1):
            if arr[i][1] <= j:
                for k in range(i):
                    dp[i][j] = max(dp[k][j], dp[i][j], dp[k][j - arr[i][1]] + arr[i][0], dp[i][j - 1])
    print(dp[n][m])