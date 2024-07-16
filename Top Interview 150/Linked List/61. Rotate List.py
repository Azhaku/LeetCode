"""
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        
        if not head:
            return head
        
        # step-1: find the length of array
        fp = head
        count = 1
        while fp.next:
            fp = fp.next
            count +=1
        k = k%count

        if k==0:
            return head
        
        # step-2: find the new tail    
        sp = head
        for _ in range(count-k-1):
            sp = sp.next
        
        # step-3: create new head ptr, set tails next as null, connect last node and first node in original
        
        nextHead = sp.next
        sp.next = None
        fp.next = head

        return nextHead
        

