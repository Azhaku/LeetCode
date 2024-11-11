import java.util.*;
class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int gcdlen = gcd(str1.length(), str2.length());

        // get the common string using the gcd found
        String gcdStr = str1.substring(0, gcdlen);

        // check the gcdString is dividing the both strings are not
        if(str1.equals(gcdStr.repeat(str1.length()/gcdlen)) &&
            str2.equals(gcdStr.repeat(str2.length()/gcdlen))){
                return gcdStr;
            }
        return "";

    }
    public int gcd(int a, int b){
        while(b!=0){
            int rem = a%b;
            a = b;
            b = rem;
        }
        return a;
    }
}