# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        # total = 0
        s = ""
        
        def helper( root, s):
            
            if not root:
                return 0
            
            s += str(root.val)
            
            if not root.left and not root.right:
                return (int(s))
            
            return helper(root.left, s) + helper(root.right,s)
        
        return helper(root,s)

        