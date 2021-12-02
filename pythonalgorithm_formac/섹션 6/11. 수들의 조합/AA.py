import sys
# sys.stdin = open("input.txt", "r")


def dfs(lev, srt):
    global sumV, cnt
    if lev == k:
        if sumV % m == 0:
            cnt += 1
    else:
        for i in range(srt, n):
            sumV += arr[i]
            dfs(lev + 1, i + 1)
            sumV -= arr[i]

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    sumV = 0
    cnt = 0
    dfs(0, 0)
    print(cnt)


