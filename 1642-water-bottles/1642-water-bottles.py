class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = (numBottles - 1) // (numExchange-1) 
        return numBottles + n
        