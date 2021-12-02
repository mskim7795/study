import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n, m = map(int, input().split())

    arr = list([10000] * (n + 1) for _ in range(n + 1))\

    for i in range(n + 1):
        arr[i][i] = 0

    for _ in range(m):
        s, e, cost = map(int, input().split())
        arr[s][e] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] == 10000:
                print("M", end=" ")
            else:
                print(arr[i][j], end=" ")
        print()
