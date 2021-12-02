import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n = int(input())
    stone = list(list(map(int, input().split())) for _ in range(n))
    stone.sort(reverse=True)
    stone.insert(0, [0, 0, 0])

    dp = [0] * (n + 1)
    dp[1] = stone[1][1]
    for i in range(2, n + 1):
        maxV = 0

        for j in range(1, i):
            if stone[i][2] < stone[j][2]:
                maxV = max(maxV, dp[j])
        dp[i] = maxV + stone[i][1]
    print(max(dp))


