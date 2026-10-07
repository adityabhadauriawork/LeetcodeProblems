class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Count the number of misplaced left and right parentheses
        left_rem = 0
        right_rem = 0
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        result = set()

        def dfs(index, left_count, right_count, left_rem_left, right_rem_left, current_path):
            # If we reach the end of the string
            if index == len(s):
                if left_rem_left == 0 and right_rem_left == 0:
                    result.add(current_path)
                return

            char = s[index]

            # Case 1: Remove the current parenthesis if allowed
            if char == '(' and left_rem_left > 0:
                dfs(index + 1, left_count, right_count, left_rem_left - 1, right_rem_left, current_path)
            if char == ')' and right_rem_left > 0:
                dfs(index + 1, left_count, right_count, left_rem_left, right_rem_left - 1, current_path)

            # Case 2: Keep the current character
            # If it's a regular character or a valid parenthesis state
            if char != '(' and char != ')':
                dfs(index + 1, left_count, right_count, left_rem_left, right_rem_left, current_path + char)
            elif char == '(':
                dfs(index + 1, left_count + 1, right_count, left_rem_left, right_rem_left, current_path + char)
            elif char == ')' and left_count > right_count:
                dfs(index + 1, left_count, right_count + 1, left_rem_left, right_rem_left, current_path + char)

        dfs(0, 0, 0, left_rem, right_rem, "")
        return list(result)
