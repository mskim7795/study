import sys
# sys.stdin = open("input.txt", "r")


def dfs(sumV, idx):
    global cnt
    if idx == k:
        if sumV == t:
            cnt += 1
    elif sumV > t:
        return
    else:
        dfs(sumV, idx + 1)
        for _ in range(arr[idx][1]):
            sumV += arr[idx][0]
            dfs(sumV, idx + 1)


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    arr = list(tuple(map(int, input().split())) for _ in range(k))
    cnt = 0
    dfs(0, 0)
    print(cnt)







