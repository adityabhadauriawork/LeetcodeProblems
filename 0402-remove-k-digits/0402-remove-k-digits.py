class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        # Traverse each digit
        for digit in num:

            # Remove larger previous digits if current digit is smaller
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            # Add current digit
            stack.append(digit)

        # If k is still left, remove digits from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Convert stack to string
        ans = "".join(stack)

        # Remove leading zeros
        ans = ans.lstrip("0")

        # If the string becomes empty, return "0"
        return ans if ans else "0"