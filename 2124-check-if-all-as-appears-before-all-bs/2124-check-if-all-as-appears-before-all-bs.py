class Solution:
    def checkString(self, s: str) -> bool:
        # print(list(s))
        # print(sorted(s))
        return list((s)) == sorted(s)
        