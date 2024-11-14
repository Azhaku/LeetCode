class Solution {
    public int largestAltitude(int[] gain) {
        int res =0;
        int sum=0;
        for(int i:gain){
            sum +=i;
            res = Math.max(res, sum);
        }
        return res;
    }
}