from collections import defaultdict
from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    max_f = max(f for f, _ in items)
    min_p = min(p for _, p in items)

    cnt = [0] * (max_f + 1)
    for f, _ in items:
      cnt[f] += 1

    total_multiples = [0] * (max_f + 1)
    for i in range(1, max_f + 1):
      if cnt[i]:
        for j in range(i, max_f + 1, i):
          total_multiples[i] += cnt[j]

    
    promo_counts = defaultdict(int)
    for f, price in items:
      if price < 2 * min_p:
        free_eligibles = total_multiples[f] - 1
        if free_eligibles > 0:
          promo_counts[price] += free_eligibles

    ans = 0
    for price in sorted(promo_counts):
      if budget < price:
        break
      can_buy = min(promo_counts[price], budget // price)
      ans += 2 * can_buy
      budget -= can_buy * price

    ans += budget // min_p

    return ans
