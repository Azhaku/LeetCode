"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
 
        #step 1: iterate LL to left ptr
        dummy = ListNode(0,head)
        leftNode, cur = dummy, head
        for i in range(left-1):
            leftNode, cur = cur, cur.next
        
        #step 2: reverse the given range of elementss
        prev = None
        for i in range(right - left + 1):
            nextNode = cur.next
            cur.next = prev
            prev,cur = cur, nextNode
        
        #step 3: update the head and tail
        leftNode.next.next = cur
        leftNode.next = prev
        return dummy.next        
        