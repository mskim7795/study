import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = 0
e = n - 1

while True:
    tmp = (e+s)//2
    if m < arr[tmp]:
        e = tmp - 1
    elif m > arr[tmp]:
        s = tmp + 1
    else:
        print(tmp + 1)
        break
