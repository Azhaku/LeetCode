"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0,head)
        group_prev = dummy
        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            print(group_prev)
            prev, cur = kth.next,group_prev.next
            while cur != group_next:
                temp = cur.next
                cur.next = prev
                prev, cur= cur,temp
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            # print(dummy)
        return dummy.next


    def getKth(self,group_prev,k):
        while k>0 and group_prev:
            group_prev = group_prev.next
            k -=1
        return group_prev