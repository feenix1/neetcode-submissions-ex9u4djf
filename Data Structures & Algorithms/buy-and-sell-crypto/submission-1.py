class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxProfit = 0
        for i in range(0, len(prices)):
            if i == 0:
                continue
            profit = prices[i] - lowestPrice
            if profit > maxProfit:
                maxProfit = profit
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]
        return maxProfit