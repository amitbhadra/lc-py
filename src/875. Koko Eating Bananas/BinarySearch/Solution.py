class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
                if hours > h:
                    return False
            return True

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
