class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_count, close_count, current_string):
            # Base case: if the string length is 2 * n, we have a valid combination
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # Add an open parenthesis if we haven't used all n open brackets
            if open_count < n:
                backtrack(open_count + 1, close_count, current_string + "(")
                
            # Add a closing parenthesis if it doesn't exceed the number of open brackets
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_string + ")")
                
        backtrack(0, 0, "")
        return res
