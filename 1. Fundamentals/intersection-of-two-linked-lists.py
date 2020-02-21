# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #strategy is just put all the nodes in a hashset (can use identity? ask teacher)
        my_set = set()
        while headA:
            my_set.add(headA)
            headA = headA.next
        
        while headB:
            if headB in my_set:
                return headB
            else:
                headB= headB.next
        
        return None
            