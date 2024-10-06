'''
Neetcode (https://neetcode.io/problems/singlyLinkedList)
Design singly linked list
'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        '''
        Dummy/Sentinel node
        a placeholder node that does not hold actual data relevant to the list's elements. 
        Instead, it serves as a convenient starting point for various operations, such as 
        inserting or deleting nodes.
        
        If it was empty: 
        (empty list)
        head -> None
        
        If there was a dummy node:
        head (dummy) -> None
        head (dummy) -> node(3) -> None
        '''
        self.head = ListNode(-1)   
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next  # Start from the first actual node
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next # Shifting the current head into the new head for ex: 1->2->3, 1->1->2->3
        self.head.next = new_node # Update the head’s next to the new node
        if not new_node.next: # Check if the New Node is the Only Node
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail == self.head:  # If list is empty
            self.head.next = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head 
        # Traverse to the node before the one we want to remove
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            # If the node to be removed is the tail, update the tail
            if curr.next == self.tail:
                self.tail = curr
            # Remove the node by bypassing it
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> list:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res