class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        if prices is None:
            return 0
        buy = prices[0]

        for i in range(len(prices)):
            if(prices[i]<buy):
                buy = prices[i]
            elif(prices[i]-buy > maxi):
                maxi = prices[i]-buy
            
        return maxi


        