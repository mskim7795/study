import sys
# sys.stdin = open("input.txt", "r")


def dfs(dt, sumV):
    global res, i

    if dt > n + 1:
        return
    else:
        res = max(res, sumV)
        for i in range(dt, n + 1):
            dfs(i + arr[i][0], sumV + arr[i][1])

if __name__ == "__main__":
    n = int(input())
    arr = [(0, 0)]
    for i in range(n):
        arr.append(tuple(map(int, input().split())))
    res = 0
    dfs(1, 0)
    print(res)
