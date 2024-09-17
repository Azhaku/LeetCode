// method 1:
// --------
class Solution {
    public int tribonacci(int n) {
        // if(n==0)
        //     return 0;
        if(n<2)
            return n;
        if(n==2)
            return 1;
        int n1 = 0,n2 = 1,n3 = 1, sum=0;
        for(int i=3;i<=n;i++){
            sum = n1+n2+n3;
            n1 = n2;
            n2 = n3;
            n3 = sum;
            // System.out.println(i+","+n1+","+n2+","+n3);
        }
        return sum;

    }
}



// method 2:
class Solution1{
    public int tribonacci(int n){
        int arr[] = {0,1,1};
        for(int i= 3; i<=n; ++i)
            arr[i%3] = arr[0]+arr[1]+arr[2];
        return arr[n%3];
    }
}