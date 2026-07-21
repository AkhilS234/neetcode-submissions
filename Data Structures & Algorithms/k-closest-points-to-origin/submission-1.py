import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        self.minHeap = []
        result = []
        p = 0

        while (p < len(points)):
            x1, y1 = points[p]
            dist1 = math.sqrt(math.pow(x1-0, 2) + math.pow(y1-0, 2))
            heapq.heappush(self.minHeap, ([dist1, x1, y1]))
            p += 1

        while (k > 0):
            dist, x, y = heapq.heappop(self.minHeap)
            result.append([x,y])
            k -= 1
        
        return result