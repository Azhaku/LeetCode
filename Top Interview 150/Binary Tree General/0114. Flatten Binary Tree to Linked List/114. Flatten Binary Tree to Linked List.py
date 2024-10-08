# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):
            if not root:
                return None
            # print(root.val)
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            # print(leftTail.val if leftTail else None)
            # print(rightTail.val if rightTail else None)
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            result = rightTail or leftTail or root
            return result
        dfs(root)

                