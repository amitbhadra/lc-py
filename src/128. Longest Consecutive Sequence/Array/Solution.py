class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        visited = set()
        for n in nums:
            if n in visited:
                continue
            if n-1 not in num_set:
                length = 1
                while n+1 in num_set:
                    length += 1
                    visited.add(n)
                    n += 1
                max_length = max(max_length, length)
        return max_length
