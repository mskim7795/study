import sys
# sys.stdin=open("input.txt", "r")

n = int(input())

arr = list(map(int, input().split()))
res = list()

prime = [0 for i in range(100001)]
prime[1] = 1

for i in range(2, 100000):
    if prime[i] == 0:
        j = 2 * i
        while j <= 100000:
            prime[j] = 1
            j += i

def reverse(x):
    tmp = 0
    res = 0
    while True:
        tmp = x % 10
        res = res * 10 + tmp
        x //= 10
        if x == 0:
            return res

def isPrime(y):
    if prime[y] == 0:
        return True
    else:
        return False

for i in arr:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')

