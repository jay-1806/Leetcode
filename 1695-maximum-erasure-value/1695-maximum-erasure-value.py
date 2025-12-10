class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        maxSum = 0
        current_sum = 0 

        # 3, 4, 5, 3
        for right in range(len(nums)):
            while nums[right] in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

            seen.add(nums[right])
            current_sum += nums[right]

            maxSum = max(current_sum, maxSum)
        return maxSum


        


