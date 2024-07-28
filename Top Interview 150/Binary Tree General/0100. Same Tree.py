"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using recursive dfs
# class Solution(object):
#     def isSameTree(self, p, q):
#         if not p and not q:
#             return 1
#         elif not p or not q or q.val != p.val:
#             return 0
#         return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

# using bfs
# class Solution(object):
#     def isSameTree(self, p, q):
#         queue = deque([[p,q]])
#         while queue:
#             dp,dq = queue.popleft()
#             if not dp and not dq:
#                 continue
#             if not dp or not dq or dp.val != dq.val:
#                 return 0
#             queue.append([dp.left,dq.left])
#             queue.append([dp.right,dq.right])

#         return 1


# using dfs
class Solution(object):
    def isSameTree(self, p, q):
        queue = [[p,q]]
        while queue:
            dp,dq = queue.pop()
            if not dp and not dq:
                continue
            if not dp or not dq or dp.val != dq.val:
                return 0
            queue.append([dp.left,dq.left])
            queue.append([dp.right,dq.right])
            print(queue)

        return 1