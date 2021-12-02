import sys
# sys.stdin = open("input.txt", "r")


def dfs(lev, word):
    global cnt
    if lev >= len(arr):
        print(word)
        cnt += 1
        return
    else:
        dfs(lev + 1, word + chr(arr[lev] + 64))
        if lev < len(arr) - 1 and arr[lev] * 10 + arr[lev + 1] <= 26:
            dfs(lev + 2, word + chr(arr[lev] * 10 + arr[lev + 1] + 64))

if __name__ == "__main__":
    n = input()
    arr = list()
    cnt = 0
    if n == 0:
        sys.exit(0)
    for x in n:
        if x == "0":
            arr.append(arr.pop() * 10)
        else:
            arr.append(int(x))
    dfs(0, "")
    print(cnt)





