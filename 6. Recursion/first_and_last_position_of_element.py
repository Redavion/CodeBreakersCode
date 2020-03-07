class Solution:
    
    def binarySearch(self, nums, lo, hi, target):
        while lo <= hi:
            mid = (lo + hi) //2
            if nums[mid] == target:
                    return mid
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        return -1
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums)-1
        findNumber = self.binarySearch(nums, lo, hi, target)
        
        if findNumber == -1:
            return [-1,-1]
        
        leftindx = findNumber
        while leftindx != lo:
            newindx = self.binarySearch(nums, lo, leftindx-1, target)
            if newindx == -1:
                break
            leftindx = newindx
        
        
        rightindx = findNumber
        while rightindx != hi:
            newindx = self.binarySearch(nums, rightindx+1, hi, target)
            if newindx == -1:
                break
            rightindx = newindx
            
        
        return [leftindx, rightindx]
        