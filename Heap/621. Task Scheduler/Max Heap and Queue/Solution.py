class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get count of each unique task
        alphaCount = {}
        for t in tasks:
            count = alphaCount.get(t, 0) + 1
            alphaCount[t] = count

        # implement max heap using min heap by adding negative values
        # we want to process more frequent jobs first
        maxHeap = []
        for k, v in alphaCount.items():
            heappush(maxHeap, (-v, k))

        # queue will store previously processed tasks as [(time, value, taskAlpha)]
        queue = collections.deque()
        time = 0
        while maxHeap or queue:
            time += 1
            while queue and queue[0][0] <= time:
                queueTask = queue.popleft()
                heappush(maxHeap, (queueTask[1], queueTask[2]))
            if maxHeap:
                task = heappop(maxHeap)
                if task[0] != -1:
                    queue.append((time+n+1, task[0]+1, task[1]))

        return time
