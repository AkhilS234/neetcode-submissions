class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = prices[0]
        if len(prices) < 2:
            return 0
        maxProfit = 0

        for i in range(1, len(prices)):
            nextPrice = prices[i]

            if nextPrice < minBuy:
                minBuy = nextPrice
            
            newProfit = nextPrice - minBuy
            maxProfit = max(newProfit, maxProfit) 
        
        if maxProfit > 0:
            return maxProfit
        else:
            return 0 