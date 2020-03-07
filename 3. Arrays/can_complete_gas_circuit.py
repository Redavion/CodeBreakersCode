class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalTank = currentTank = start = 0
        for i in range(len(gas)):
            totalTank += gas[i] - cost[i]
            currentTank += gas[i] - cost[i]

            if currentTank < 0:
                #we can't make it from this starting point
                start = i+1
                currentTank = 0


        return start if totalTank >= 0 else -1