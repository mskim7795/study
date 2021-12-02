import sys
from collections import deque
# sys.stdin = open("input.txt", "r")




if __name__ == "__main__":

    n = int(input())
    arr = [0] * (n + 1)

    rt = list(map(int, input().split()))
    rt.insert(0, 0)
    rt[1] = 1

    for i in range(2, n + 1):
        maxV = 0
        for j in range(1, i):
            if rt[j] < rt[i]:
                maxV = max(maxV, arr[j])
        arr[i] = maxV + 1

    print(max(arr))

