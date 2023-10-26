# https://leetcode.com/problems/last-stone-weight/

# DO NOT USE MAX HEAP
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [s * -1 for s in stones]
        heapify(minHeap)

        while len(minHeap) > 1:
            w1, w2 = heappop(minHeap), heappop(minHeap)
            if w1 != w2:
                heapq.heappush(minHeap, -1 * abs(w1 - w2))

        return abs(minHeap[0]) if minHeap else 0
