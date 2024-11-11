class Solution {
    public boolean canPlaceFlowers(int[] fb, int n) {
        for(int i=0; i<fb.length; i++){
            boolean left = i==0 || fb[i-1] == 0;
            boolean right = i==fb.length-1 || fb[i+1] == 0;
            if(left && right && fb[i]==0){ 
                fb[i] = 1;
                n--;
            }
        }
        return n<=0;
    }
}