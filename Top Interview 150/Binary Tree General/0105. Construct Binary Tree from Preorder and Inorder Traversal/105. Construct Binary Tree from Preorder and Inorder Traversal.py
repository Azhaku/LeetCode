# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def splitTree(self,preorder, inorder_dic, root_idx, left, right):
        
        # with the root index create first root/subroot
        root = TreeNode(preorder[root_idx])

        #  get mid value
        mid = inorder_dic[preorder[root_idx]]

        #  get left Nodes if exists
        if mid> left:
            root.left = self.splitTree(preorder, inorder_dic, root_idx+1, left,mid -1)
        #  get right nodes if exists
        if mid<right:
            root.right = self.splitTree(preorder, inorder_dic, root_idx+mid - left +1, mid+1, right)
        return root

    def buildTree(self, preorder, inorder):
        inorder_dic = {}
        for i in range(0, len(inorder)):
            inorder_dic[inorder[i]] = i
        return self.splitTree(preorder, inorder_dic, 0,0, len(inorder)-1)
    