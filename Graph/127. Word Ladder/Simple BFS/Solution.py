# TLE
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        visited = set()

        def findDiff(a, b):
            diff = 0
            if len(a) != len(b):    return max(len(a), len(b))
            for i in range(len(a)):
                if a[i] != b[i]:    diff += 1
            return diff

        queue = collections.deque()
        queue.append(beginWord)
        print(queue)
        res = 1
        while queue:
            queueLen = len(queue)
            res += 1
            for i in range(queueLen):
                startWord = queue.popleft()
                print(res, startWord)
                if startWord in visited:    continue
                visited.add(startWord)
                for word in wordList:
                    if word not in visited and findDiff(startWord, word) == 1:
                        if word == endWord: return res
                        queue.append((word))
                visited.add(startWord)
        return 0
