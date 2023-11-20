# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr):
            i = 0 
            j = len(arr)-1
            while i<=j:
                mid = (i+j)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]>target:
                    j = mid-1
                else:
                    i = mid+1
            return False
        for i in range(len(matrix)):
            if matrix[i][0]<=target<=matrix[i][-1]:
                if binary_search(matrix[i]):
                    return True
            elif matrix[i][0]>target:
                return False
        return False
