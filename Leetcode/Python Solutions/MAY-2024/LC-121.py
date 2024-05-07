class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 1:
            return 0
        left = 0
        right = left+1
        profit = 0
        while right < length:
            if prices[right] < prices[left]:
                left = right
            if prices[right] > prices[left]:
                profit = max(profit,prices[right]-prices[left])
            right+=1
        return profit
        