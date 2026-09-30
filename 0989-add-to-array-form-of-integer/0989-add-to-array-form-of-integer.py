class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        while k:
            k, remainder = divmod(k, 10)
            num.insert(0, remainder)
        return num
