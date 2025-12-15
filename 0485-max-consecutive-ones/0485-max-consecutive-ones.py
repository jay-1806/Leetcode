class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        curr_len = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                l += 1
                r += 1
                curr_len = 0

            else:
                curr_len += 1
            res = max(res, curr_len)
        return res
        