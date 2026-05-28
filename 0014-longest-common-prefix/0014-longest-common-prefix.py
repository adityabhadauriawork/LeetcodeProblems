class Solution:
    def longestCommonPrefix(self, strs):
        ans = ""

        if strs is None:
            return ""

        for i in range(len(strs[0])):
            for a in strs:
                if i == len(a) or a[i] != strs[0][i]:
                    return ans

            ans = ans + strs[0][i]

        return ans