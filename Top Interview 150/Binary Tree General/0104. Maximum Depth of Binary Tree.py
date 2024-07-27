"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


# method 1: Recursive DFS ,refer: neetcode yt

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return  1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        # return  1 + min(self.maxDepth(root.left),self.maxDepth(root.right))  # Minimum depth of a binary tree
     
        # Visiting Node with value: 3
        # Visiting Node with value: 9
        # Node value 9 -> Left Depth: 0, Right Depth: 0, Result: 1
        # Visiting Node with value: 20
        # Visiting Node with value: 15
        # Node value 15 -> Left Depth: 0, Right Depth: 0, Result: 1
        # Visiting Node with value: 7
        # Node value 7 -> Left Depth: 0, Right Depth: 0, Result: 1
        # Node value 20 -> Left Depth: 1, Right Depth: 1, Result: 2
        # Node value 3 -> Left Depth: 1, Right Depth: 2, Result: 3
        # Maximum Depth: 3
    

# method 2: BFS 
from collections import deque
class Solution1(object):
    def maxDepth(self,root):
        if not root:
            return 0
        level = 0
        q = deque([root])
        # debug_q = deque([root.val])
        while q:
            for i in range(len(q)):
                # print(len(q))
                node = q.popleft()
                # debug_q.popleft()
                if node.left:
                    # debug_q.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    # debug_q.append(node.right.val)
                    q.append(node.right)
                # for finding minimum depth
                # if not node.right and not node.left:
                #     return level + 1
            # print(debug_q)
            level += 1
        return level


# method 3: Iterative DFS
class Solution2(object):
    def maxDepth(self,r):
        stack = [[r,1]]
        res = 0
        m_depth = float('inf')
        while stack:
            node,depth = stack.pop()
            # print(node,depth,node.val if node else None)

            if node:
                # for minimum depth
                # if not node.left and not node.right:
                #     m_depth = min(depth,m_depth)
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return [res,m_depth]

#create binary tree
# [3,9,None,None,20,15,7]
t = TreeNode(3)
td = t
td.right = TreeNode(9)
td.left = TreeNode(20)
# td.left.right = TreeNode(22)
# td.left.left = TreeNode(21)
td = td.right
td.right = TreeNode(15)
td.left = TreeNode(7)
# print(t.val,t.right.val,t.left.val)

print("""
         3
        / \\
      20   9
          / \\
         7   15
         
      """)

s = Solution()
print(s.maxDepth(t))

s = Solution1()
print(s.maxDepth(t))

s = Solution2()
print(s.maxDepth(t))