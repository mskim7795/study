import sys
# sys.stdin=open("input.txt", "r")

str = input()
num = 0
count = 0
for x in str:
    if x >= '0' and x <= '9':
        num = num * 10 + int(x)

for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print(num, count, sep='\n')







