import sys
# sys.stdin = open("input.txt", "r")
n = 0
res = 0
arr = []
check = False
def DFS(x, s):
    if s == res:
        global check
        check = True
    if x == n:
        return
    else:
        DFS(x + 1, s + arr[x])
        DFS(x + 1, s)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    res = sum(arr) / 2
    sumV = 0
    DFS(0, sumV)
    if check:
        print("YES")
    else:
        print("NO")


