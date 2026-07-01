class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        l1=set(freq.values())
        l1=list(l1)
        l2=list(freq.values())
        l2.sort()
        l1.sort()
        return l1==l2        