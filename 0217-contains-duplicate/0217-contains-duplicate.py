class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False



















        n = len(nums)
        numbers = set()
        for i in range(n):
            if i in numbers:
                return True

            numbers.add(i)
        
        return False

         