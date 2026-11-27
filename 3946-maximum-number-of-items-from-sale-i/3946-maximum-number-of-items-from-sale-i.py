from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    n = len(items)
    frees = [0] * n
    for i in range(n):
      for j in range(n):
        if i != j and items[j][0] % items[i][0] == 0:
          frees[i] += 1
    dp = [0] * (budget + 1)
    for i in range(n):
      price = items[i][1]
      first_val = 1 + frees[i]
      for b in range(budget, price - 1, -1):
        if dp[b - price] + first_val > dp[b]:
          dp[b] = dp[b - price] + first_val
      for b in range(price * 2, budget + 1):
        if dp[b - price] + 1 > dp[b]:
          dp[b] = dp[b - price] + 1
    return max(dp)
