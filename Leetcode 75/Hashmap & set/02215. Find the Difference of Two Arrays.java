import java.util.*;

class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> map1 = new HashSet<>();
        Set<Integer> map2 = new HashSet<>();
        List<Integer> temp = new LinkedList<>();
        List<Integer> temp1 = new LinkedList<>();

        for(int i:nums1){
            map1.add(i);
        }

        for(int i:nums2){
            map2.add(i);
        }

        // update the nums1 diff
        for(int i:map1){
            if(!map2.contains(i)){
                    temp.add(i);
            }
        }
        // update the nums2 diff
        for(int k:map2){
            if(!map1.contains(k)){
                    temp1.add(k);
            }
        }

        List<List<Integer>> temp2 = new ArrayList<>();
        temp2.add(temp);
        temp2.add(temp1);
        return temp2;

    
    }

}