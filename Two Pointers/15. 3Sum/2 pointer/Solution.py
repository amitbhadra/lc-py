class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            # Skip duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    part = ((nums[i], nums[l], nums[r]))
                    output.append(part)
                    l += 1
                    # skip duplicates
                    while nums[l-1]==nums[l] and l<r:
                        l += 1
                        
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return output
