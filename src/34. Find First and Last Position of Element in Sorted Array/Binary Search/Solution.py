class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def b_search(l, r, left_bias=True):
            res = -1
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    res = mid
                    if left_bias:
                        r = mid
                    else:
                        l = mid + 1
            return res

        return [b_search(0, len(nums)), b_search(0, len(nums), False)]
