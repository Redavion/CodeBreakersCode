import heapq
class KthLargest(object):
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pq = []
        self.k = k
            
        for i in range(min(len(nums),k)):
            heapq.heappush(self.pq, nums[i])

        for i in range(k, len(nums)):
                if nums[i] > self.pq[0]:
                    heapq.heappop(self.pq)
                    heapq.heappush(self.pq, nums[i])
                    

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pq) < self.k:
            heapq.heappush(self.pq,val)
        elif val > self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq,val)
        return self.pq[0]
        
