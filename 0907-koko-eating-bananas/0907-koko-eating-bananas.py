class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeNeeded(k: int) -> int:
            total_hours = 0 
            for pile in piles:
                total_hours += ceil(pile/k)
            return total_hours

        low = 1
        high = max(piles) if piles else 1
        ans = high

        while low <= high:
            k = (low+high) // 2
            hours_spent = timeNeeded(k)

            if hours_spent <= h:
                ans = k  
                high = k - 1
            else:
                low = k+1

        return ans


        