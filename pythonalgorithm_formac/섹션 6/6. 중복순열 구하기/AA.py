import sys
# sys.stdin = open("input.txt", "r")


def bt(x):
    global cnt
    if len(x) == m:
        for i in range(m):
            print(x[i], end=" ")
        cnt += 1
        print()
        return
    else:
        for i in range(1, n + 1):
            x.append(i)
            bt(x)
            x.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    bt([])
    print(cnt)

