'''
Neetcode(https://neetcode.io/problems/reverse-a-linked-list)
Leetcode(https://leetcode.com/problems/reverse-linked-list/)
Reverse Linked List

Given the beginning of a singly linked list head, reverse the list, and return the new 
beginning of the list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    
s = Solution()
print(s.reverseList([0,1,2,3]))
print(s.reverseList([]))