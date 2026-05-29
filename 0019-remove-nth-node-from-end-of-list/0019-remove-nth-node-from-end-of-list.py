# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #approach = take two pointer , one at head and second one at head to and give it a early start ok
        # nth times , than when that pointer will point none , your first pointer would be just one node before at what you have to delete
        p1 = head
        p2 = head
        for i in range(n):
            p2=p2.next
        if p2==None:   #corner case what that n is the lenght of total nodes list
            head = head.next
            return head
        while p2.next!=None:
            p2=p2.next
            p1=p1.next
        p1.next=p1.next.next
        return head
        