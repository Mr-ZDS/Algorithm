class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i , j = 0 , 1
        result = 0
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
            else:
                if result < (prices[j] - prices[i]):
                    result = prices[j] - prices[i]
            j += 1
        return result