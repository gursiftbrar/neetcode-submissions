class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0 
        right = left + 1

        max_profit = 0

        while right < len(prices):

            profit = prices[right] - prices[left]

            if max_profit < profit:
                max_profit = profit 

            elif prices[right] < prices[left]:
                left = right
            
            right += 1
        
        return max_profit



        