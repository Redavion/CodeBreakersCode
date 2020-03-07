class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        lo = 0
        hi = len(matrix) * len(matrix[0]) - 1
        
        while lo <= hi:
            middle = (lo + hi)//2
            middleElement = matrix[middle//len(matrix[0])][middle%len(matrix[0])]
            if middleElement == target:
                return True
            elif middleElement < target:
                lo = middle+1
            elif middleElement > target:
                hi = middle-1
        return False