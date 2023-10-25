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

        # create patterns
        wordList.append(beginWord)
        patterns = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                patterns[pattern].append(word)

        queue = collections.deque()
        queue.append(beginWord)
        res = 1
        while queue:
            queueLen = len(queue)
            res += 1
            for i in range(queueLen):
                startWord = queue.popleft()
                if startWord in visited:    continue
                visited.add(startWord)
                for j in range(len(startWord)):
                    pattern = startWord[:j] + '*' + startWord[j+1:]
                    for word in patterns[pattern]:
                        if word not in visited and findDiff(startWord, word) == 1:
                            if word == endWord: return res
                            queue.append((word))
                visited.add(startWord)
        return 0
