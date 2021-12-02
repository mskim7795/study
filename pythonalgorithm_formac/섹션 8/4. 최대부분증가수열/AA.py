import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    dp = [1] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        maxV = 1
        for j in range(1, i):
            if arr[j] < arr[i]:
                maxV = max(maxV, dp[j] + 1)
        dp[i] = maxV

    print(max(dp))
