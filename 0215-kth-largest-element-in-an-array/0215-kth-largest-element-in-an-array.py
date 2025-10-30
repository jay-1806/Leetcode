class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        nums = (-i for i in nums)
        for i in nums:
            maxHeap.append(i)
        heapq.heapify(maxHeap)

        res = []
        while k > 0:
            x = heapq.heappop(maxHeap)
            res.append(x)
            k -=1

        return -res[-1]
            