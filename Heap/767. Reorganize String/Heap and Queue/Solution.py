class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:   return ""
        charCount = {}
        for c in s:
            count = charCount.get(c, 0)
            charCount[c] = count + 1
        
        maxHeap = []
        for k, v in charCount.items():
            heapq.heappush(maxHeap, (v * -1, k))

        res = " "
        queue = collections.deque()
        i = 0
        while len(res) != len(s)+1:
            while queue and queue[0][0] <= i:
                item = queue.popleft()
                heapq.heappush(maxHeap, (item[1], item[2]))
            if maxHeap and maxHeap[0][1] == res[-1]:
                item = heapq.heappop(maxHeap)
                queue.append((i+1, item[0], item[1]))
            if not maxHeap: return ""
            mostUsedItem = heapq.heappop(maxHeap)
            res += mostUsedItem[1]
            if mostUsedItem[0] != -1:
                queue.append((i+2, mostUsedItem[0]+1, mostUsedItem[1]))
            i += 1

        return res[1:]
