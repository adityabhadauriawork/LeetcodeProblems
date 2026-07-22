class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        best = [float('inf')] * n
        prefix = {0: -1}
        s = 0
        ans = float('inf')
        cur = float('inf')

        for i in range(n):
            s += arr[i]
            if s - target in prefix:
                length = i - prefix[s - target]
                cur = min(cur, length)
            best[i] = cur
            prefix[s] = i

        prefix = {0: -1}
        s = 0
        cur = float('inf')

        for i in range(n):
            s += arr[i]
            if s - target in prefix:
                length = i - prefix[s - target]
                if prefix[s - target] >= 0:
                    ans = min(ans, length + best[prefix[s - target]])
            prefix[s] = i

        return ans if ans != float('inf') else -1