class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # this only works if we have guarantee that array is [1..n, n]
        # this won't work here
        # expected = (len(nums)-1) * (len(nums)) / 2
        # return int(sum(nums)-expected)

        # def get_looped_index(i):
        #     if i >= len(nums):
        #         return i - len(nums)
        #     return i

        slow = fast = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
