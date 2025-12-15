class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[0:k])
        max_sum = current_sum

        for i in range(k,len(nums)):
            leaving_element = nums[i-k]
            entering_element = nums[i]
            current_sum = current_sum - leaving_element + entering_element

            max_sum = max(max_sum, current_sum)
        return max_sum / k

