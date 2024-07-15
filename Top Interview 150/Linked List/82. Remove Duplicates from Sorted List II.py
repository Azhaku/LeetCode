"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# method 1: two pointer: beats 87%
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next
    
# method 2:
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0,head)
        cur = dummy
        while cur and cur.next and cur.next.next:
            fn = cur.next
            sn = cur.next.next
            duplicate = False

            #  skip the duplicate nodes
            while fn and sn and fn.val== sn.val:
                sn = sn.next
                duplicate = True
            
            # update new node
            if duplicate:
                cur.next = sn
            else:
                cur = cur.next

        return dummy.next