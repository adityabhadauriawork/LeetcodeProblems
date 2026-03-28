class Solution:
    def Pow(self,x,n):
        #base case
        if n==0:
            return 1
        #recursive case
        a = self.Pow(x,n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*x

    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            return self.Pow(x,n)
        else:
            return 1/self.Pow(x,-(n))

        