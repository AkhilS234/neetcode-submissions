from collections import defaultdict
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        hash_table = {}
        hash_table = defaultdict(int)
        time = 0
        queue = deque()

        for t in tasks:
            hash_table[t] += 1

        maxHeap = [-k for k in hash_table.values()]
        heapq.heapify(maxHeap)

        while (maxHeap or queue):
            time += 1
            if maxHeap:
                maxVal = heapq.heappop(maxHeap)
                count = 1 + maxVal
                if (count != 0):
                    queue.append([count, time + n])

            if (queue and (queue[0][1] == time)):
                x,y = queue.popleft()
                heapq.heappush(maxHeap, x)

        return time