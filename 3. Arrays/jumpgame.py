class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        best_index = 0
        for i in range(len(nums)):
            if i > best_index:
                return False
            best_index = max(best_index, nums[i]+i) 
        return True