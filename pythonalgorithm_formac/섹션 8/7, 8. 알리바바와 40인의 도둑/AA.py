import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n = int(input())
    board = list(list(map(int, input().split())) for _ in range(n))

    dp = list([2147000000] * n for _ in range(n))
    dp[0][0] = board[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + board[i][0]
        dp[0][i] = dp[0][i - 1] + board[0][i]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + board[i][j]
    print(dp[n - 1][n - 1])

