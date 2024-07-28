"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 """
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # recursive dfs
# class Solution(object):
#     def mirror(self, l,r):
#         if not r and not l:
#             return 1
#         elif not l or not r or l.val!= r.val:
#             return 0
#         return (self.mirror(l.left,r.right) and self.mirror(l.right,r.left))
        
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return self.mirror(root.left,root.right)

# # iterative dfs
# class Solution(object):
#     def isSymmetric(self,root):
#         stack = [[root.left,root.right]]
#         while stack:
#             r, l = stack.pop()
#             if not r and not l:
#                 continue
            
#             # breaking condition
#             if not r or not l or r.val != l.val:
#                 return 0

#             # add new node values
#             stack.append([l.left, r.right])
#             stack.append([l.right,r.left])
#         return 1


# bfs
class Solution(object):
    def isSymmetric(self,root):
        queue = [[root.left, root.right]]
        while queue:
            l , r = queue.pop(0)
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return 0
            queue.append([l.left,r.right])
            queue.append([l.right,r.left])
        return 1