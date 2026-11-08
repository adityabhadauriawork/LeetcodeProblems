class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        ones = [i for i, x in enumerate(nums) if x == 1]
        n = len(ones)
        
        c = 0
        for i, x in enumerate(nums):
            if x == 1:
                cur = 1
                if i > 0 and nums[i-1] == 1: cur += 1
                if i + 1 < len(nums) and nums[i+1] == 1: cur += 1
                c = max(c, cur)
        
        c = min(c, k)
        if maxChanges >= k - c:
            return max(0, c - 1) + (k - c) * 2
            
        l = k - maxChanges
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + ones[i]
            
        ans = float('inf')
        for i in range(n - l + 1):
            j = i + l - 1
            mid = (i + j) // 2
            med = ones[mid]
            left_cnt = mid - i
            right_cnt = j - mid
            cost = (med * left_cnt - (pref[mid] - pref[i])) + ((pref[j + 1] - pref[mid + 1]) - med * right_cnt)
            ans = min(ans, cost)
            
        return ans + maxChanges * 2