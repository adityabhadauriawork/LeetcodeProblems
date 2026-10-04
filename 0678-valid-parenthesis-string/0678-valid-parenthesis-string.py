class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            elif char == '*':
                # '*' can be ')', which reduces the open count
                min_open -= 1
                # '*' can be '(', which increases the open count
                max_open += 1
            
            # If max_open is negative, there are too many closing brackets.
            # No possible wildcard substitution can save this string.
            if max_open < 0:
                return False
            
            # min_open cannot carry over as negative because we can't have 
            # less than 0 open brackets. If it goes below 0, it means we chose 
            # to treat some '*' as ')' when we should have treated them as "".
            if min_open < 0:
                min_open = 0
                
        # The string is valid if we can form a perfect balance (min_open reaches 0)
        return min_open == 0
