package Array;
class Solution {
    public int arrayNesting(int[] nums) {
        int high = 0;
        for(int i = 0;i<nums.length;i++){
            if(nums[i]!= -1){
                high = Math.max(high, traversal(nums, i));
            }
        }
        return high;
    }
    public int traversal(int[] nums, int j){
        if(nums[j] == -1 || j < 0)
            return 0;
        int temp = nums[j];
        nums[j] = -1;
        return 1+(traversal(nums, temp));
    }
}