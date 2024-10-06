class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinked:
    def __init__(self):
        '''
        Dummy/Sentinel node: 
        A placeholder node that simplifies operations by eliminating edge cases 
        when inserting or removing nodes from an empty list or the head of the list.
        
        With the dummy node, an empty list looks like this:
        head (dummy) <-> None
        And a list with elements looks like:
        head (dummy) <-> node1 <-> node2 <-> None
        '''
        self.head = ListNode(-1)  # Dummy node, doesn't store actual data
        self.tail = self.head     # Initially tail is the same as head

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
        '''
        Two Edge Cases
        1. If the list is not empty
        2. If the list is empty
        '''
        new_node = ListNode(val)
        new_node.next = self.head.next  # Connect the new node to the current first node
        
        if self.head.next:
            self.head.next.prev = new_node  # If list is not empty, set the current first node's prev to new_node
        
        self.head.next = new_node  # Update head to point to the new first node
        new_node.prev = self.head  # Set the new node's prev to the head (dummy node)
        
        if self.tail == self.head:  # If the list was empty, update the tail
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail == self.head:  # If list is empty (only dummy node)
            self.head.next = new_node
            new_node.prev = self.head
        else:
            self.tail.next = new_node  # Set the current tail's next to the new node
            new_node.prev = self.tail  # Set the new node's prev to the current tail
        
        self.tail = new_node  # Update the tail to the new node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head.next  # Start at the first real node
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr:  # We have found the node to remove
            # Update the previous node's next to skip the current node
            if curr.prev:
                curr.prev.next = curr.next
            # If curr is not the last node, update the next node's prev to skip the current node
            if curr.next:
                curr.next.prev = curr.prev
            # If curr was the tail, update the tail pointer
            if curr == self.tail:
                self.tail = curr.prev
            return True
        return False

    def getValues(self) -> list:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res