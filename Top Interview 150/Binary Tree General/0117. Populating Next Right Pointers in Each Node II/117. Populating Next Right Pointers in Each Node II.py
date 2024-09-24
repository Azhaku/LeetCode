"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# bfs
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        lst = deque([root])
        while lst:
            n = len(lst)
            # print(n)
            for i in range(n):
                cur = lst.popleft()
                # get left and right
                if cur:
                    if cur.left:
                        lst.append(cur.left)
                    if cur.right:
                        lst.append(cur.right)
                    # print(cur, lst)
                    if(i != n-1):
                        cur.next = lst[0]
        return root
    
    
    
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        cur = root
        prev, head = None, None
        
        while cur:
            while cur:
                if not prev:
                    head = cur.left if cur.left else cur.right
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right
                
                cur = cur.next

            prev = None
            cur = head

        return root