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
        Node cur = root, nxt = (root != null)?root.left:null;
        while(cur!= null && nxt != null){
            cur.left.next = cur.right;
            if(cur.next!= null){
                cur.right.next = cur.next.left;
            }
            cur = cur.next;
            if(cur == null){
                cur = nxt;
                nxt = cur.left;
            }
        }
        return root;
    }
}

// method 2: using queue in java
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
        Queue<Node> que = new LinkedList<>();
        if(root == null){
            return root;
        }
        que.offer(root); //adds value without raising exception
        root.next = null;
        while(!que.isEmpty()){ 
            int n = que.size();
            for(int i=0;i<n;i++){
                Node poll = que.poll(); //remove and get first element from 

                if(poll.left != null){
                    que.offer(poll.left);
                    poll.next = que.peek(); // see the first element without removing it 
                }
                if(poll.right != null){
                    que.offer(poll.right);
                }
                poll.next = que.peek();
                if(i == n-1){
                    poll.next = null;
                }


            }
        }

        return root;
    }
}