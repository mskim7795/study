import sys
# sys.stdin=open("input.txt", "r")

n = int(input())
res = []
num = 0
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    check = 1
    for j in range(2):
        if check == 1 and arr[j] == arr[j+1]:
            check = 2
            num = arr[j]
        elif check == 2 and arr[j] == arr[j+1]:
            check = 3

    if check == 1:
        res.append(arr[2] * 100)
    elif check == 2:
        res.append(1000 + num * 100)
    else:
        res.append(10000 + num * 1000)

res.sort(reverse=True)
print(res[0])



