class Solution(object):
    
    def findMinHelper(self, nums, low, hi, minimum):
            if low > hi:
                return minimum
            
            mid = (low+hi)//2
            if nums[mid] < minimum:
                minimum = nums[mid]
            #if the pivot exists on the left side, 
            if nums[low] < nums[hi]:
                return min(minimum, nums[low])
            if  nums[low]> nums[mid]:
                return self.findMinHelper(nums, low, mid-1, minimum)
            return self.findMinHelper(nums, mid+1, hi, minimum)
                
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return None
    
        return self.findMinHelper(nums, 0, len(nums)-1, float("inf"))
        
        