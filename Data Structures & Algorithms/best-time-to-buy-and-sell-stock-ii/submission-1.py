class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        leftPtr = 0
        rightPtr = 1
        total = 0

        while ((leftPtr < rightPtr) and (rightPtr < len(prices))):
            leftPrice = prices[leftPtr]
            rightPrice = prices[rightPtr]

            if (leftPrice < rightPrice):
                total += (rightPrice - leftPrice)

            leftPtr += 1
            rightPtr += 1

        return total

# Runtime: O(n) as each index is checked once
# Space Compplexity: O(1), no extra data structures created

    