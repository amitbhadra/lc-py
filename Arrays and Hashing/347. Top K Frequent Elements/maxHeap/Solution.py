# https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = collections.Counter(nums)
        count_list = []
        for key in count_dict:
            count_list.append([count_dict[key]*-1, key])
        heapq.heapify(count_list)
        i =0 
        ret = []
        while i<k:
            ret.append(heapq.heappop(count_list)[1])
            i+=1
        return ret
