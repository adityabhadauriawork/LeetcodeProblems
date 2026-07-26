# class Solution:
#     def climbStairs(self, n: int) -> int:
#         freq={
#             0:0,
#             1:1,
#             2:2,
#             3:3
#         }
#         def f(x):
#             if x in freq:
#                 return freq[x]
#             else:
                
#                 freq[x] = f(x-1) + f(x-2)
#                 return freq[x]
#         return f(n)

        # FIXED MEMORY , TABULIZATION
class Solution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        prev = 2
        curr = 3
        for i in range(4,n+1):
            prev,curr = curr,prev+curr
        return curr


