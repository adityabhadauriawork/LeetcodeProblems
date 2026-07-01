class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        count = list(freq.values())   
        return len(count) == len(set(count))     