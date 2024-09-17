# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def splitTree(self, postorder, inorder_dic, root_idx, left, right):
        if left > right:  # Base case: no elements to construct the tree
            return None
        
        # The root is the last element in the current postorder slice
        root_val = postorder[root_idx]
        root = TreeNode(root_val)

        # Get the index of the root in inorder traversal
        mid = inorder_dic[root_val]

        # Recursively build the right subtree first
        if mid < right:
            root.right = self.splitTree(postorder, inorder_dic, root_idx - 1, mid + 1, right)
        
        # Recursively build the left subtree
        if mid > left:
            root.left = self.splitTree(postorder, inorder_dic, root_idx - (right - mid) - 1, left, mid - 1)

        return root

    def buildTree(self, inorder, postorder):
        # Create a dictionary to quickly find the index of a value in inorder
        inorder_dic = {val: idx for idx, val in enumerate(inorder)}
        # Start from the last element of the postorder array
        return self.splitTree(postorder, inorder_dic, len(postorder) - 1, 0, len(inorder) - 1)
