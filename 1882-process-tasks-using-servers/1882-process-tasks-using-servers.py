import heapq
from typing import List


class Solution:

  def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
    idle = [(weight, i) for i, weight in enumerate(servers)]
    heapq.heapify(idle)

    busy = []
    ans = []

    for j, t in enumerate(tasks):
      while busy and busy[0][0] <= j:
        _, weight, idx = heapq.heappop(busy)
        heapq.heappush(idle, (weight, idx))

      if idle:
        weight, idx = heapq.heappop(idle)
        heapq.heappush(busy, (j + t, weight, idx))
      else:
        free_time, weight, idx = heapq.heappop(busy)
        heapq.heappush(busy, (free_time + t, weight, idx))

      ans.append(idx)

    return ans
