import sys
# sys.stdin = open("input.txt", "r")

arr = list(range(0, 21))

for i in range(10):
    a, b = map(int, input().split())
    for j in range((b-a+1)//2):
        arr[a+j], arr[b-j] = arr[b-j], arr[a+j]

for i in range(1, 21):
    print(arr[i], end=' ')






