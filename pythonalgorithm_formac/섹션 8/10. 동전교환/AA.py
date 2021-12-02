import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n = int(input())

    arr = list(map(int, input().split()))

    m = int(input())

    dp = [2147000000] * (m + 1)

    for i in range(1, m + 1):
        for j in range(n):
            if i > arr[j]:
                dp[i] = min(dp[i], dp[i - arr[j]] + 1)
            elif i == arr[j]:
                dp[i] = 1
    print(dp[m])

