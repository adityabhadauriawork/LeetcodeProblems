class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ""

        for ch in s:
            if ch.isalnum(): # alnum only allows numbers and alphabet
                new_s = new_s + ch.lower()

        rev = ""

        for i in range(len(new_s)-1, -1, -1):
            rev = rev + new_s[i]

        if new_s == rev:
            return True

        return False