class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxscore = 0;
        
        if len(A) < 3:
            return maxscore
        
        start = 0;
        upwardslope = False
        peak = False
        
      
        for i in range(1,len(A)):
            if A[i]==A[i-1]:
                upwardslope = False
                peak = False
                start = i
            elif A[i] > A[i-1]:
                if peak:
                    start = i-1
                    peak = False
                upwardslope = True
            else:
                peak = upwardslope
                if not peak:
                    start = i
                else: 
                    maxscore = max(maxscore, i-start + 1)
        return maxscore
                    