class Solution:
    def climbStairs(self, n: int) -> int:
        freq={
            0:0,
            1:1,
            2:2,
            3:3
        }
        def f(x):
            if x in freq:
                return freq[x]
            else:
                
                freq[x] = f(x-1) + f(x-2)
                return freq[x]
        return f(n)