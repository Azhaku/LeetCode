# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        cur = res
        carry = 0
        sum = 0
        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum+= l2.val
                l2=l2.next
            carry = sum//10
            # sum = sum%10
            cur.next = ListNode(sum%10)
            cur = cur.next
        if carry == 1:
            cur.next = ListNode(carry)
        return res.next    
                
l1 = ListNode()
l11 = l1
l2 = ListNode()
l22 = l2
val = [5,5,5]
for i in val:
    l11.next = ListNode(i)
    l11 = l11.next
    l22.next = ListNode(i)
    l22 = l22.next

s = Solution()
res = s.addTwoNumbers(l1.next,l2.next)
while res:
    print(res.val)
    res = res.next

# while l1:
#     print(l1.val)
#     print(l2.val)
#     l1 = l1.next
#     l2 = l2.next


