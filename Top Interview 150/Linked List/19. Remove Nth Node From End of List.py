"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# method 1: more than 1 traversal(find the length of LL)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        cur = dummy
        if not head.next:
            return head.next
        
        # find the length of LL
        length = -1
        while cur:
            cur = cur.next
            length +=1
            
        # go to the n-1 th Node
        cur = dummy
        for i in range(length-n):
            cur = cur.next
        print(cur)
        
        # change the LL ptr
        cur.next = cur.next.next if cur.next != None else None
        return dummy.next

# with dummy node
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        fn = dummy
        sn = dummy
        
        # move second pointer n spaces ahead 
        for i in range(n):
            sn = sn.next

        while sn.next:
            sn = sn.next
            fn = fn.next
        
        fn.next = fn.next.next
        return dummy.next
    
    
# fully optimized
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fn = head
        sn = head
        
        # handle edge case: when there is only one element is there. no need to run remaing code
        if not head.next:
            return head.next
        
        # move second pointer n spaces ahead 
        for i in range(n):
            sn = sn.next
        
        # handle edge case: where sn straighly went upto null. means remove the first node.
        if not sn:
            return head.next

        while sn.next:
            sn = sn.next
            fn = fn.next
        
        fn.next = fn.next.next
        return head
