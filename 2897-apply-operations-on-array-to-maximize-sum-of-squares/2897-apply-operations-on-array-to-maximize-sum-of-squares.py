class Solution:

  def maxSum(self, nums: list[int], k: int) -> int:
    MOD = 1_000_000_007
    MAX_BIT = 30

    bit_count = [0] * MAX_BIT
    for num in nums:
      for i in range(MAX_BIT):
        if (num >> i) & 1:
          bit_count[i] += 1

    ans = 0
    for _ in range(k):
      current_num = 0
      for i in range(MAX_BIT):
        if bit_count[i] > 0:
          current_num |= 1 << i
          bit_count[i] -= 1
      ans = (ans + current_num * current_num) % MOD

    return ans
