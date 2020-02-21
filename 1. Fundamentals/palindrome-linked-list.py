# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def palindromeHelper(myList): #why cant i call this
        return True
    
    def isPalindrome(self, head: ListNode) -> bool:
        myList = []
        #iterate through linked list
        while head:
            myList.append(head.val)
            head = head.next
        
        #reverse = myList.reverse()
        return myList == myList[::-1]