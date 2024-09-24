/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumNumbers(TreeNode root) {
        return (findSum(root, 0));
    }
    public int findSum(TreeNode root,int num){
        if(root == null)
            return 0;
        num = (num*10) + root.val;
        // System.out.println(num+","+root.val);
        if(root.right == null && root.left ==null)
            return num;
        return (findSum(root.right, num) + findSum(root.left, num));
    }
}