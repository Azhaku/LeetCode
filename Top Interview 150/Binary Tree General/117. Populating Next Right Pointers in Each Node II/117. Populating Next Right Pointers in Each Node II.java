/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root == null)
            return root;
        Queue<Node> kue = new LinkedList<>();
        kue.offer(root);
        root.next = null;
        while(!kue.isEmpty()){
            int n = kue.size();
            for(int i=0; i<n; i++){
                Node poll = kue.poll();
                if(poll != null){
                    if(poll.left != null)
                        kue.offer(poll.left);
                    if(poll.right != null)
                        kue.offer(poll.right);
                    if(n-1 != i)
                        poll.next = kue.peek();
                }
            }
        }
        return root;
    }
}