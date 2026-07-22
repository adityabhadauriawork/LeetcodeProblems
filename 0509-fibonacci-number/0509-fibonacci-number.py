class Solution:
    def fib(self, n: int) -> int:
        #BASE CASE'S
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # dp = [0]*(n+1)
        # dp[0] = 0
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]
                                # time = 0(n)    space = 0(n)
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev = 0
        curr = 1
        for i in range(2,n+1):
            prev , curr = curr , prev +  curr
        return curr

                                # TIME = 0(n)   SPACE = 0(1)

        