import sys
# sys.stdin = open("input.txt", "r")

l = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()

for _ in range(m):
    arr[0] += 1
    arr[l-1] -= 1
    i = 0
    while arr[i] > arr[i + 1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 1
    i = l - 1
    while arr[i] < arr[i-1]:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1
print(arr[l-1] - arr[0])
