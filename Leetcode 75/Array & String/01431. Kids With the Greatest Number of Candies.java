import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        ArrayList<Boolean> li = new ArrayList<>();
        int max = Arrays.stream(candies).
            reduce(Integer::max).orElse(0);
        for(int i:candies){
            li.add(i+extraCandies >= max? true: false);
        }
        return li;
    }
}