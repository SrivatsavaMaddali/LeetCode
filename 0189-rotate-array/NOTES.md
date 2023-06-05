//Initially solved this question in another way:
class Solution {
    public void rotate(int[] nums, int k) {
     int l=nums.length;
        int[] temp = new int[l];
        for(int p=0;p<l;p++){
            temp[p]=nums[p];
        }
        int realrot;
        realrot=(k<l)?k:k%l;
        for(int i=realrot;i>0;i--){
            for(int j=1;j<l;j++){
                nums[j]=temp[j-1];
            }
            nums[0]=temp[l-1];
            
            for(int p=0;p<l;p++){
            temp[p]=nums[p];
        }
        }
        
    }
}
//But this code time complexity is very high. It works well with smaller arrays but with bigger arrays, it will exceed the time limits.
