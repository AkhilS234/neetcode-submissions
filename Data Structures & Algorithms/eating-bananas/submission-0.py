class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        right = max(piles)
        left = 1
        output = 0
        while (left <= right):
            mid_k = (left + right) // 2
            num_hours = 0

            for pile in piles:
                num_hours += math.ceil(pile/mid_k)

            if (num_hours <= h):
                output = mid_k
                right = mid_k-1
            else: 
                if (num_hours > h):
                    left = mid_k + 1
                
        return output
                


                


