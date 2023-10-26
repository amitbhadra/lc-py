# Beats 5%

class Point:
    def __init__(self, point):
        self.point = point
    def __lt__(self, other):
        selfDist = sqrt(self.point[0]**2 + self.point[1]**2)
        otherDist = sqrt(other.point[0]**2 + other.point[1]**2)
        return selfDist < otherDist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coords = []
        for p in points:
            coords.append(Point(p))
        heapify(coords)
        res = []
        while k > 0 and coords:
            res.append(heappop(coords).point)
            k -= 1
        return res
