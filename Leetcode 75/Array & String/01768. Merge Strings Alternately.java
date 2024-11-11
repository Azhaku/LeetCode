class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int count=0;
        while((word1.length()>count) || (word2.length()>count)){
            if(count < word1.length()){
                sb.append(word1.charAt(count));
            }
            if(count < word2.length()){
                sb.append(word2.charAt(count));
            }
            count++;
        }
        return sb.toString();
    }
}
