# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        minHeap = []
        for num in nums_dict:
            if len(minHeap) >= k:
                heapq.heappushpop(minHeap, (nums_dict[num], num))
            else:
                heapq.heappush(minHeap, (nums_dict[num], num))
        return [key for val, key in minHeap]
