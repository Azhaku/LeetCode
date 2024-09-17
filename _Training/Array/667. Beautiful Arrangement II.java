package Array;

//method 1
// n =10, k =2
// [1,10,9,8,7,6,5,4,3,2]
// [1,10,2,3,4,5,6,7,8,9]
// [1,10,2,9,8,7,6,5,4,3]
class Solution {
    public int[] constructArray(int n, int k) {
        int[] arr= new int[n];
        // for(int i= 0; i < n; i++){
        //     arr[i] = i+1;
        // }
        int low = 1,high = n, index = 0;
        arr[index++] = low++;
        byte isHigh = 0;
        while(k>1){
            arr[index++] = high--;
            k--;
            isHigh = 1;
            if (k>1){
                isHigh = 0;
                arr[index++] = low++;
                k--;
            }
        }
        while(index<n){
            if(isHigh == 1){
                arr[index++] = high--;
            }
            else
                arr[index++] = low++;
        }

        return arr;
    }
}

//method 2

class Solution1 {
    public int[] constructArray(int n, int k) {
      int ans[]=new int[n];
      int left=1;
      int right=n;
      int i=0;
      while(k!=1){
        if(i%2==0){
            ans[i]=right;
            right--;
        }else{
            ans[i]=left;
            left++;
        }
        i++;
        k--;
      }
      if (i % 2 == 0) {
            while (right >= left) {
                ans[i] = right;
                right--;
                i++;
            }
        } else {
            while (right >= left) {
                ans[i] = left;
                left++;
                i++;
            }
        }
        return ans;

    }
}