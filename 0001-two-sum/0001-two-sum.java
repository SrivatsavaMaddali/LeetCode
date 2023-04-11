class Solution {
    public int[] twoSum(int[] nums, int target)
    {
        int flag=-2;
        int sol[]=new int[2];
        sol[0]=10000;
        sol[1]=10000;
        int rem,i,j;
        int n=nums.length;
        for(i=0;i<n;i++)
        {
                rem=target-nums[i];
                for(j=i+1;j<n;j++)
                {
                    if(nums[j]==rem)
                    {
                        flag=j;
                        break;
                    }
                    else
                    {
                        
                        flag=-1;
                    }
                }
                if(flag==-1)
                    continue;
                else
                {
                    sol[0]=i;
                    sol[1]=j;
                    
                    break;
                }
        }
        return sol;
    }
}