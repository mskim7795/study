import sys
import heapq
# sys.stdin = open("input.txt", "r")
minH = []
while True:
    num = int(input())
    if num == 0:
        if minH:
            tmp = heapq.heappop(minH)
            print(tmp[1])
        else:
            print(-1)
    elif num == -1:
        break
    else:
        heapq.heappush(minH, (-num, num))