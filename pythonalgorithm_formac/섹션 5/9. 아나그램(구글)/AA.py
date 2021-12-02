import sys
# from collections import deque
# sys.stdin = open("input.txt", "r")

word1 = list(input())
word2 = list(input())
hash1 = dict()
hash2 = dict()

for x in word1:
    if hash1.get(x, 0) == 0:
        hash1[x] = 1
    else:
        hash1[x] += 1
for x in word2:
    if hash2.get(x, 0) == 0:
        hash2[x] = 1
    else:
        hash2[x] += 1
check = True
for x in word1:
    if hash1.get(x, 0) != hash2.get(x, 0):
        print("NO")
        check = False
        break
if check:
    print("YES")
