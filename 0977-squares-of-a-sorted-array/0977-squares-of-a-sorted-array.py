class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left , right = 0 , n-1

        for i in range(n-1, -1, -1):
            left_sq = nums[left]*nums[left]
            right_sq = nums[right]*nums[right]

            if left_sq > right_sq:
                result[i] = left_sq
                left += 1
            else:
                result[i] = right_sq
                right -= 1
        return result