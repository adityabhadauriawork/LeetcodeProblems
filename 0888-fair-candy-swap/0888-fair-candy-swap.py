class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        b = set(bobSizes)
        for x in aliceSizes:
            if x - diff in b:
                return [x, x - diff]