# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Edge case: Empty list or list with only one node
        if not head or not head.next:
            return head
        
        # Initialize pointers
        odd = head            # Keeps track of the last node in the odd chain
        even = head.next      # Keeps track of the last node in the even chain
        even_head = even      # Remembers the start of the even chain to connect later
        
        # Traverse the list until there are no more even nodes or next elements
        while even and even.next:
            odd.next = even.next   # Connect the current odd node to the next odd node
            odd = odd.next         # Move the odd pointer forward
            
            even.next = odd.next   # Connect the current even node to the next even node
            even = even.next       # Move the even pointer forward
            
        # Connect the end of the odd chain to the head of the even chain
        odd.next = even_head
        
        return head
