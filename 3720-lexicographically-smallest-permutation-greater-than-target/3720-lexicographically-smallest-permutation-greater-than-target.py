from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        src = Counter(s)
        tgt = Counter(target)
        
        def dfs(idx):
            nonlocal src, tgt
            if idx == n - 1:
                r_chars = sorted(src.keys())
                t_char = target[idx]
                for ch in r_chars:
                    if ch > t_char:
                        return ch
                return ""
            
            t_char = target[idx]
            candi = sorted([ch for ch in src.keys() if ch >= t_char])
            
            for ch in candi:
                src[ch] -= 1
                if src[ch] == 0:
                    src.pop(ch)
                
                # Check if it matches target or is strictly greater
                if ch == t_char:
                    res = dfs(idx + 1)
                    if res != "":
                        return ch + res
                else:
                    # Greedily take the rest sorted
                    rest = []
                    for k in sorted(src.keys()):
                        rest.extend([k] * src[k])
                    return ch + "".join(rest)
                
                # Backtrack
                src[ch] += 1
            
            return ""

        return dfs(0)
