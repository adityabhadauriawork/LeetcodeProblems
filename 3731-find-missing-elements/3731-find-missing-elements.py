class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)
        mn = min(nums)
        mx = max(nums)
        ans = []
        for x in range(mn + 1, mx):
            if x not in present:
                ans.append(x)
        return ans