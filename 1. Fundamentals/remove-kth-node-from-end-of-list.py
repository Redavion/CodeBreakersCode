# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        runner = head
        count = 0
        #get runner into position
        while count < n:
            runner = runner.next
            count += 1
        
        prev = None
        cur = head
        
        while runner:
            runner = runner.next
            prev = cur
            cur = cur.next

        if prev is None:
            return cur.next
        
        prev.next = cur.next
        return head
        