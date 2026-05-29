# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # brutalforce solution
        curr = head
        counter = 0

        while curr != None:
            curr = curr.next
            counter = counter + 1

        if counter % 2 == 0:
            counter = (counter // 2)
        else:
            counter = (counter // 2)   # CHANGED: removed +1 because it was moving extra step

        curr2 = head                   # CHANGED: removed "head = counter"

        for i in range(counter):       # CHANGED: used loop to move till middle node
            curr2 = curr2.next

        return curr2                   # CHANGED: directly return middle node