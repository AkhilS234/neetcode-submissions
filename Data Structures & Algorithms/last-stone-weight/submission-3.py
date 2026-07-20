import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        self.maxHeap = stones
        heapq.heapify_max(self.maxHeap)

        while len(self.maxHeap) > 1:

            x = heapq.heappop_max(self.maxHeap)
            y = heapq.heappop_max(self.maxHeap)

            if (x!=y):
                diff = abs(x-y)
                heapq.heappush_max(self.maxHeap, diff)

        if not self.maxHeap:
            return 0
        else:
            return self.maxHeap[0]