import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        self.maxHeap = nums
        heapq.heapify_max(self.maxHeap)
        num = 0

        while(k > 0):
            num = heapq.heappop_max(self.maxHeap)
            k -= 1

        return num