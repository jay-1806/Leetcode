class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2 = []

        for num in nums:
            nums2.append(num*num)

        nums2.sort()
        return nums2
        