# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        first_half = head
        second_half = slow

        prev = None
        current = second_half

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first = first_half
        second = prev

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True