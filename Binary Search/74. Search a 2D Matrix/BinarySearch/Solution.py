class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n
        while left < right:
            mid = left + (right - left) // 2
            mid_x = mid // n
            mid_y = mid % n
            if matrix[mid_x][mid_y] == target:
                return True
            elif matrix[mid_x][mid_y] > target:
                right = mid
            else:
                left = mid + 1

        return False
