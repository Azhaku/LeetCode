class Solution {
    public boolean increasingTriplet(int[] nums) {
        if(nums.length < 3)
            return false;

        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;
        
        for(int i = 0;i<nums.length;i++)
        {
            if(nums[i] <= min1) min1 = nums[i];
            else if(nums[i] <=min2) min2 = nums[i];
            else return true;
        }
        return false;
    }
}

//min1=99999
//min2=99999
//[20,100,10,12,5,13]
//min1=5
//min2=12
//nums.length=6
