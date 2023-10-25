class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        left, right = 1, totalTrips * min(time)

        def condition(maxTime):
            numTrips = 0
            for t in time:
                trips = maxTime // t
                if trips == 0:  break
                numTrips += trips
                if numTrips >= totalTrips:  return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
