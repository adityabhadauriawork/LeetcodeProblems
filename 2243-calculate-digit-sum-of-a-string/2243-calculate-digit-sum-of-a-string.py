class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                chunk = s[i : i + k]
                total = 0
                for char in chunk:
                    total += int(char)
                new_s += str(total)
            s = new_s
        return s