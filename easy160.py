# given the heads of two singly linked lists headA and headB
# return the node at which the two lists intersect
# if the two linked lists have no intersection at all, return null

# the test cases are generated such that
# there are no cycles anywhere in the entire list structure

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if headA is None or headB is None:
            return None
        
        nodeA = headA
        nodeB = headB
        
        # need to loop twice
        # once to find the length of each list
        # and a second time to loop over while at an equal distance from the end of each list
        # swapping the pointers for the second loop accomplishes this
        
        while nodeA is not nodeB:
            
            if nodeA is None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            
            if nodeB is None:
                nodeB = headA
            else: nodeB = nodeB.next
        
        # either nodeA is nodeB or nodeA is nodeB is None
        return nodeA