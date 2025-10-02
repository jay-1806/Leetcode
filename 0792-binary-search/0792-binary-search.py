class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index, i in enumerate(nums):
            if i == target:
                return index
            else:
                index += 1
        return -1


        