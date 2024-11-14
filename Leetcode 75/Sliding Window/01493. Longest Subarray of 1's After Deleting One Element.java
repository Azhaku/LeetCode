class Solution {
    public int longestSubarray(int[] nums) {
        /*

            0,1,1,1,0,1,1,0,1
            0 3 2 1
            3 5 3

            step1 : count the continous 1s
            step2 : maintain a max sum of last count + curr count
            step3 : max of them is the answer

        */

        int lastCount = 0;
        int currCount = 0;
        int maxSum = 0;

        for(int n : nums){

            if(n == 0){
                // in 0 we will skip so the subarray of 1 will be
                // last 1s count + current 1s count
                maxSum = Math.max(maxSum, lastCount + currCount);
                lastCount = currCount;
                currCount = 0;
            }else{
                // count 1s
                currCount++;
            }
        }

        maxSum = Math.max(maxSum, lastCount + currCount);

        // incase its all 1s
        if(maxSum == nums.length) maxSum = maxSum-1;

        return maxSum;
    }
}


class Solution2 {
    public int longestSubarray(int[] nums) {
        int mco = 0, left = 0; 
        int zero_found = 0;
        for(int i =0; i<nums.length; i++){
            zero_found += nums[i] == 0? 1 : 0;
            while(zero_found>1){
                zero_found -= nums[left] == 0? 1 : 0;
                left++;
            }
            mco = Math.max(mco, i-left);
            System.out.println(i-left);
        }
        return mco;
    }
}