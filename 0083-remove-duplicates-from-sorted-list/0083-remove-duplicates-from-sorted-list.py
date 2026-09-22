# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        temp= head
        prev=None
        while temp.next is not None:
            if temp.val== temp.next.val:
                temp.next= temp.next.next
            else:
                temp=temp.next

        return head