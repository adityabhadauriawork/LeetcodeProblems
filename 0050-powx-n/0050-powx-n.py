class Solution:
    def Pow(self,x,n):
        #base case
        if n==0:
            return 1
        #recursive case
        a = self.Pow(x,n//2)
        # if 2,10 then -> 10//2 = 5 there fore return (2^5)^2 since odd therefore * 2
        if n%2==0:
            return a*a
        else:
            return a*a*x

    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            return self.Pow(x,n)
        else:
            return 1/self.Pow(x,-(n))

        