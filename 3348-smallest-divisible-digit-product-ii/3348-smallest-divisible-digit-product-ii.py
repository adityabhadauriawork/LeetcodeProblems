from math import gcd

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Check if t contains prime factors other than 2, 3, 5, 7
        temp = t
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                temp //= p
        if temp > 1:
            return "-1"
        
        n = len(num)
        
        # left_t[i] stores the remaining required product factor for the suffix starting at index i
        left_t = [0] * (n + 1)
        left_t[0] = t
        
        # Locate the first '0' if it exists
        first_zero_idx = n
        for i, char in enumerate(num):
            if char == '0':
                first_zero_idx = i
                break
            # Compute remaining t required after considering the current digit
            d = int(char)
            left_t[i + 1] = left_t[i] // gcd(left_t[i], d)
            
        # Case A: If num contains no zeros and its digit product is already divisible by t
        if first_zero_idx == n and left_t[n] == 1:
            return num
            
        # Helper function to find the minimum digits needed to satisfy a remaining factor
        def get_min_suffix_digits(required_t: int) -> list:
            suffix = []
            for d in range(9, 1, -1):
                while required_t % d == 0:
                    suffix.append(str(d))
                    required_t //= d
            return suffix[::-1]  # Return sorted ascendingly (smallest numbers first)

        # Case B: Try to modify num at some position from right to left to make it larger
        # We start checking from the first zero index (or the end of the string if no zeros)
        for i in range(min(first_zero_idx, n - 1), -1, -1):
            curr_digit = int(num[i])
            
            # Try to increment the current digit to find a valid larger prefix
            for next_digit in range(curr_digit + 1, 10):
                rem_t = left_t[i] // gcd(left_t[i], next_digit)
                min_suffix = get_min_suffix_digits(rem_t)
                
                # Check if the remaining suffix fits into the remaining slots
                slots_left = n - 1 - i
                if len(min_suffix) <= slots_left:
                    # Pad with '1's to fill empty spaces cleanly
                    padding_count = slots_left - len(min_suffix)
                    final_suffix = ['1'] * padding_count + min_suffix
                    
                    return num[:i] + str(next_digit) + "".join(final_suffix)
                    
        # Case C: If no modifications within the same length worked, the answer must be longer
        min_suffix = get_min_suffix_digits(t)
        # Ensure it is at least 1 digit longer than num
        target_len = max(n + 1, len(min_suffix)) 
        padding_count = target_len - len(min_suffix)
        
        return "1" * padding_count + "".join(min_suffix)
