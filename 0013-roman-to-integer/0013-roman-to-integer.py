class Solution:
    def romanToInt(self, s: str) -> int:
        maal = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000

        }
        ans = 0
        for i in range(len(s)):
            if i < len(s)-1 and maal[s[i]] < maal[s[i+1]]:
                ans-=maal[s[i]]
            else:
                ans+=maal[s[i]]
        return ans