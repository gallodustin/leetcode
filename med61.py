# https://leetcode.com/problems/rotate-list/

# Given the head of a linked list, rotate the list to the right by k places.

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Constraints:
# * The number of nodes in the list is in the range [0, 500].
# * -100 <= Node.val <= 100
# * 0 <= k <= 2 * 109

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # sanity check
        if head is None:
            return None
        
        # get length of list and fix k using modulo
        length = 1
        cur_node = head
        while cur_node.next is not None:
            cur_node = cur_node.next
            length += 1
        if length <= k:
            k = k%length
        
        # another sanity check
        if k == 0:
            return head
        
        # "window" is the nodes at the end of the list to be moved to the beginning
        # window_start is the first node in the window
        # window_end is the last node in the window
        # window_prev is the node before the window, so that it can be updated to be the end of the list
        window_start = head
        if window_start is None:
            return None
        window_end = window_start
        for i in range(k - 1): # e.g. if k is 4 we need to get next 3 times
            window_end = window_end.next
        window_prev = None
        while window_end.next is not None:
            window_prev = window_start
            window_start = window_start.next
            window_end = window_end.next
            
        # chop the window off the end and add it to the beginning
        if window_prev is not None:
            window_prev.next = None
        window_end.next = head
        return window_start
        