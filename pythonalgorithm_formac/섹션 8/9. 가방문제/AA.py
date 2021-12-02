import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n, wei = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(n))

    dp = [0] * (wei + 1)

    for i in range(1, wei + 1):
        for j in range(n):
            if i >= arr[j][0]:
                tmp = i - arr[j][0]
                dp[i] = max(dp[tmp] + arr[j][1], dp[i])

    print(dp[wei])

