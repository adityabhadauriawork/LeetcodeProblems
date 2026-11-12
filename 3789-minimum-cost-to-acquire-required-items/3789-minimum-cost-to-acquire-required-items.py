class Solution:

  def minimumCost(
      self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
  ) -> int:
    mi = min(need1, need2)
    mx = max(need1, need2)
    return min(
        need1 * cost1 + need2 * cost2,  # Strategy 1: Buy all items separately
        mi * costBoth
        + (need1 - mi)
        * cost1
        + (need2 - mi)
        * cost2,  # Strategy 2: Use combined type for the smaller need
        mx * costBoth,  # Strategy 3: Cover everything using combined type
    )
