from bisect import bisect_left

class Solution:
    def minOperations(self, target, arr):
        pos = {x: i for i, x in enumerate(target)}

        seq = []

        for x in arr:
            if x in pos:
                idx = pos[x]
                p = bisect_left(seq, idx)

                if p == len(seq):
                    seq.append(idx)
                else:
                    seq[p] = idx

        return len(target) - len(seq)