class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1_000_000_007
        # endsIn[i] tracks the number of distinct subsequences ending with character ('a' + i)
        ends_in = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # New total subsequences ending with this character = sum of all existing subsequences + 1 (the single char itself)
            ends_in[idx] = (sum(ends_in) + 1) % MOD
            
        return sum(ends_in) % MOD
