class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        ans = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            length = (r - l) + 1
            # r+=1 r to already bhad rha hai for loop hai bro
            ans = max(ans, length)
            sett.add(s[r])
        return ans



        