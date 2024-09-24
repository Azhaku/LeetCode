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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        Queue<TreeNode> lst = new LinkedList<>();
        if(root == null)
            return false;
        // List.of(0,1)
        lst.offer(root);
        while(!lst.isEmpty()){
            int n = lst.size();
            System.out.print(n);
            for(int i=0;i<n;i++){

                // List<Object> nv = lst.poll();
                TreeNode node = lst.poll();
                int total = node.val;
                if(node.left != null){
                    node.left.val += total;
                    lst.offer(node.left);
                }
                else if(node.left == null && node.right == null && node.val == targetSum)
                    return true;
                // if(node.left != null && node.right != null)
                // System.out.println("left, right: "+node.val+", "+node.val);
                
                if(node.right != null){
                    node.right.val += total;
                    lst.offer(node.right);
                }
                else if(node.left == null && node.right == null && node.val == targetSum)
                    return true;
                
            }
        }
        return false;
    }
}