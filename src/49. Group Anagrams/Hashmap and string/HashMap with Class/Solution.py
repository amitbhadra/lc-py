import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        class Element:
            def __init__(self, n):
                self.n = n
                self.val = 0
            def __lt__(self, other):
                return self.val < other.val

        elements = {}
        for n in nums:
            if n not in elements:
                elements[n] = Element(n)
            # hack to make this maxheap
            elements[n].val -= 1

        heapmax = list(elements.values())
        heapq.heapify(heapmax)

        output = []
        for i in range(k):
            output.append(heapq.heappop(heapmax).n)

        return output
