class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [0] * (n + 1)

        def add(i, val):
            i += 1
            while i <= n:
                tree[i] += val
                i += i & (-i)

        def query(i):
            s = 0
            i += 1
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        def is_peak(i):
            if i <= 0 or i >= n - 1:
                return 0
            return 1 if nums[i] > nums[i - 1] and nums[i] > nums[i + 1] else 0

        peaks = [0] * n
        for i in range(1, n - 1):
            peaks[i] = is_peak(i)
            if peaks[i]:
                add(i, 1)

        res = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                if r - l < 2:
                    res.append(0)
                else:
                    res.append(query(r - 1) - query(l))
            else:
                idx, val = q[1], q[2]
                nums[idx] = val
                for i in range(max(0, idx - 1), min(n, idx + 2)):
                    old = peaks[i]
                    new = is_peak(i)
                    if old != new:
                        peaks[i] = new
                        add(i, new - old)
        return res