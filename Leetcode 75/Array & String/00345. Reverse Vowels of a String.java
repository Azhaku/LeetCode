
class Solution {
    public String reverseVowels(String s) {
        char[] sArr = s.toCharArray();
        int left = 0;
        String vowel = "aeiouAEIOU";
        int n = s.length();
        int right = n-1;
        while(left<right){
            // find the left vowel
            while(left< right && (vowel.indexOf(sArr[left]))==-1){
                left++;
            }
            // find the right vowel
            while(left< right && (vowel.indexOf(sArr[right]))==-1){
                right--;
            }
            char temp = s.charAt(left);
            sArr[left] = sArr[right];
            sArr[right] = temp;

            left++;
            right--;
        }
        return new String(sArr);
    }
}