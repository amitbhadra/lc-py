class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for i, n in enumerate(nums):
            if i >= k:   heappushpop(minHeap, n)
            else:   heappush(minHeap, n)
        return minHeap[0]
