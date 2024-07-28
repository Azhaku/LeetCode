"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # using recrusive dfs
# class Solution(object):
#     def invertTree(self, root):
#         if root:
#             root.right, root.left = root.left,root.right
#         else:
#             return None
#         self.invertTree(root.right)
#         self.invertTree(root.left)
#         return root



# using bfs
class Solution(object):
    def invertTree(self, root):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right , node.left
                queue.append(node.left)
                queue.append(node.right)
                print(node.val if node else None)

        return root

# # using dfs
# class Solution(object):
#     def invertTree(self, root):
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 node.left, node.right = node.right , node.left
#                 stack.append(node.left)
#                 stack.append(node.right)
#             print(node.val if node else None)
#         return root 