import sys
# sys.stdin = open("input.txt", "r")


def D(res):
    global cnt
    if len(res) == m:
        for i in res:
            print(i, end=" ")
        print()
        cnt += 1
        return
    else:
        for i in range(1, n + 1):
            check = False
            for j in res:
                if i == j:
                    check = True
                    break
            if check:
                continue
            res.append(i)
            D(res)
            res.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    D([])
    print(cnt)

