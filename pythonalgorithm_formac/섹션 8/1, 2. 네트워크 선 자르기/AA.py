import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n = int(input())

    dp = [0] * 46

    dp[1] = 1
    dp[2] = 2

    for i in range(3, 46):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])