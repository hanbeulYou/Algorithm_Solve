import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_heap, max_heap = [], []

for _ in range(N):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    if len(max_heap) > 0 and len(min_heap) > 0 and max_heap[0] * -1 > min_heap[0]:
        max_val = heapq.heappop(max_heap) * -1
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, min_val * -1)
        heapq.heappush(min_heap, max_val)

    print(max_heap[0] * -1)