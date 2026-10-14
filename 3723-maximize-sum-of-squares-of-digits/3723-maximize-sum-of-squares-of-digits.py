class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
        
        num_nines, remainder = divmod(sum, 9)
        
        ans = ["9"] * num_nines
        
        if remainder > 0:
            ans.append(str(remainder))
            
        num_zeros = num - len(ans)
        ans.extend(["0"] * num_zeros)
        
        return "".join(ans)
