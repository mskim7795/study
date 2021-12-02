import sys
import heapq
# sys.stdin = open("input.txt", "r")
minH = []

while True:
    num = int(input())
    if num == 0:
        if minH:
            print(heapq.heappop(minH))
        else:
            print(-1)
    elif num == -1:
        break
    else:
        heapq.heappush(minH, num)