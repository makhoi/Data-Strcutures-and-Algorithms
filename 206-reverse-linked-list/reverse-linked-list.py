# RECURSION METHOD

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        reversed_list_head = self.reverseList(head.next)
        # Get the last node after the list is reversed
        last_node = head.next
        # Set the current node as last node's next element
        last_node.next = head
        head.next = None

        return reversed_list_head