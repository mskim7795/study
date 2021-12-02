import sys
# sys.stdin = open("input.txt", "r")


def DFS(x, idx):
    global maxV
    if x > c:
        return
    elif maxV > x + sum(arr[idx:n]):
        return
    else:
        maxV = max(x, maxV)
        if idx == n:
            return
        DFS(x + arr[idx], idx + 1)
        DFS(x, idx + 1)


if __name__ == "__main__":
    c, n = map(int, input().split())
    arr = []
    maxV = 0
    for _ in range(n):
        arr.append(int(input()))
    DFS(0, 0)
    print(maxV)



