class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        i = 0
        j = 1

        while j != len(prices):
            if prices[i] < prices[j]:
                if max < prices[j] - prices[i]:
                    max = prices[j] - prices[i]
            else:
                i = j
            
            j += 1

        return max
