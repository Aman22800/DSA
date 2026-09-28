# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:

        # Base case:
        # A list with 0 or 1 node is already sorted
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        # fast moves twice as fast as slow
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        # 'mid' becomes the head of the second half
        mid = slow.next

        # Disconnect the two halves
        slow.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves
        # Dummy node makes merging easier
        dummy = ListNode(0)
        curr = dummy

        # Compare nodes from both lists
        # and attach the smaller node
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        # Attach whatever nodes are left
        # in either list
        curr.next = left if left else right

        # dummy itself is not part of the answer
        return dummy.next