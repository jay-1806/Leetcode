class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # if n == 2:
            return max(nums[0],nums[1])

        def robbed(nums):
            prev2 = 0
            prev1 = 0

            for money in nums:
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr

            return prev1

        case_a = robbed(nums[:-1])        
        case_b = robbed(nums[1:])

        return max(case_a,case_b)