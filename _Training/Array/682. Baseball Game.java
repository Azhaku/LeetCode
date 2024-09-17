package Array;
import java.util.ArrayList;

class Solution {
    public int calPoints(String[] operations) {
        ArrayList<Integer> arr = new ArrayList<>();
        int res = 0;

        for (int i = 0; i < operations.length; i++) {
            String op = operations[i];
            if (op.equals("D")) {
                int lastScore = arr.get(arr.size() - 1);
                arr.add(2 * lastScore);
            } 
            else if (op.equals("+")) {
                int lastScore = arr.get(arr.size() - 1);
                int secondLastScore = arr.get(arr.size() - 2);
                arr.add(lastScore + secondLastScore);
            } 
            else if (op.equals("C")) {
                arr.remove(arr.size() - 1);
            } 
            else {
                int temp = Integer.parseInt(op);
                arr.add(temp);
            }
        }
        for (int score : arr) {
            res += score;
        }

        return res;
    }
}
