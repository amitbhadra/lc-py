class Solution:
    def trap(self, height: List[int]) -> int:
        # get max height from L2R
        l2r = []
        max_ht = 0
        for n in height:
            l2r.append(max_ht)
            max_ht = max(max_ht, n)

        # get max height from R2L
        r2l = []
        max_ht = 0
        for n in height[::-1]:
            r2l.insert(0, max_ht)
            max_ht = max(max_ht, n)

        # floodwater will be min of the 2 values at the index
        area = 0
        for i in range(len(height)):
            water = min(l2r[i], r2l[i]) - height[i]
            if water > 0:
                area += water

        return area
