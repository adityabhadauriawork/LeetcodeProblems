class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # If the total number of '1's is less than k, no valid substring exists
        if s.count('1') < k:
            return ""
        
        res = ""
        min_len = float('inf')
        left = 0
        count_ones = 0
        
        # Expand the right pointer to find a valid window
        for right in range(len(s)):
            if s[right] == '1':
                count_ones += 1
                
            # Shrink from the left while the window has exactly k '1's
            while count_ones == k:
                current_len = right - left + 1
                current_str = s[left : right + 1]
                
                # Update result if a shorter or lexicographically smaller string is found
                if current_len < min_len:
                    min_len = current_len
                    res = current_str
                elif current_len == min_len:
                    if current_str < res:
                        res = current_str
                
                # Shrink the window by moving the left pointer
                if s[left] == '1':
                    count_ones -= 1
                left += 1
                
        return res
