class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to serve as the base boundary
        stack = [-1]
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:
                # Pop the top element for a matching ')'
                stack.pop()
                
                if not stack:
                    # If empty, the current ')' has no match. 
                    # Push its index as the new base boundary.
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_length = max(max_length, i - stack[-1])
                    
        return max_length
