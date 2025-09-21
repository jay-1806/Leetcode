class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        buy = prices[0]
        best = 0
        for p in prices[1:]:
            buy = min(buy, p)
            best = max(best, p - buy)
        return best




        