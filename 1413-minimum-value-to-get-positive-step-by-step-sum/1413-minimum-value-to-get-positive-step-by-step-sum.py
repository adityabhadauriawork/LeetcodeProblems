class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        run_sum = 0
        min_sum = 0

        for num in nums:
            run_sum += num
            min_sum = min(min_sum, run_sum)

        return 1 - min_sum