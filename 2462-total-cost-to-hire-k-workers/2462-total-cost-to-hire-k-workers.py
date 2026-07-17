from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        left = 0
        right = n - 1

        left_heap = []
        right_heap = []

        # Fill left heap
        while left < candidates and left <= right:
            heapq.heappush(left_heap, costs[left])
            left += 1

        # Fill right heap
        while right >= n - candidates and right >= left:
            heapq.heappush(right_heap, costs[right])
            right -= 1

        total = 0

        for _ in range(k):

            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total += heapq.heappop(left_heap)

                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total += heapq.heappop(right_heap)

                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna