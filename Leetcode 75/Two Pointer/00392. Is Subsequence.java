class Solution {
    public boolean isSubsequence(String s, String t) {

        if(s.length()==0)
            return true;
        int itr = 0;
        int idx = 0;
        while(itr<t.length() && idx<s.length()){
            if(s.charAt(idx) == t.charAt(itr++)){
                idx++;
            }
        }
        if(idx==s.length()){
                return true;
            }
        return false;
    }
}

// tip1: if you convert the string into charArray() it will be bit faster than this one
// tip2: try converting both the strings