class Solution {
    public int reverse(int x) {
        if(x>0){
            return helper(x);
        }else if(x<0){
            return -helper(x*(-1));
        }else{
            return 0;
        }
    }
    public int helper(int x){
        int result=0;
        int last=0;
        int flag=0;
        int c=0;
        while(x>0){
            last=x%10;
            if(c==0&&last>2){flag=1;}
            result=result*10+last;
            x=x/10;
            c+=1;
        }
        if(flag==1&&c==10){return 0;}
        if(result>-2147483645 && result<2147483647){
        return result;}else{
            return 0;
        }
    }
}