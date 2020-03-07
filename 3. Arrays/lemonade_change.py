class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for bill in bills:
            if bill == 20:
                if ten and five:
                    ten -=1
                    five -=1
                elif five >= 3:
                    five -=3
                else:
                    return False
            elif bill == 10:
                if five:
                    five -= 1
                    ten += 1
                else: 
                    return False
            else:
                five += 1
                
        return True