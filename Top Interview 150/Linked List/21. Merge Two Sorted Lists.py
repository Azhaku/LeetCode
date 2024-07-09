# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        tmp = res
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
        while l1:
            tmp.next = ListNode(l1.val)
            tmp = tmp.next
            l1 = l1.next
        while l2:
            tmp.next = ListNode(l2.val)
            tmp = tmp.next
            l2 = l2.next

        return res.next
                
l1 = ListNode()
l11 = l1
l2 = ListNode()
l22 = l2
val = [1,2,4]
for i in val:
    l11.next = ListNode(i)
    l11 = l11.next
    
val2 = [1,3,4]
for i in val2:
    l22.next = ListNode(i)
    l22 = l22.next
# while l1:
#     print(l1.val)
#     l1 = l1.next

s = Solution()
res = s.mergeTwoLists(l1.next,l2.next)
while res:
    print(res.val)
    res = res.next