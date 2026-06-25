class Solution:
    def reverse(self, x: int) -> int:
         
        if x==0:
            return 0
        original = x
        if x<0:
            x = (-1)*x
        ans=0
        while(x!=0):
            
            rem = x%10
            ans = ans*10
            ans += rem
            x=x//10
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        if original<0:
            ans = -1 * ans
            return ans
        else:
            return ans




        