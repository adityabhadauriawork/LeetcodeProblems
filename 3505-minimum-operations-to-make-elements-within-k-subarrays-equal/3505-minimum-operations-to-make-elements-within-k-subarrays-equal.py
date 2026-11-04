import heapq
from collections import Counter

class DualHeap:
    def __init__(self):
        self.small = []
        self.large = []
        self.delayed = Counter()
        self.small_size = 0
        self.large_size = 0
        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed[num] == 0:
                break
            heapq.heappop(heap)
            self.delayed[num] -= 1

    def balance(self):
        if self.small_size > self.large_size + 1:
            num = -heapq.heappop(self.small)
            self.small_size -= 1
            self.large_size += 1
            self.small_sum -= num
            self.large_sum += num
            heapq.heappush(self.large, num)
            self.prune(self.small)

        elif self.small_size < self.large_size:
            num = heapq.heappop(self.large)
            self.large_size -= 1
            self.small_size += 1
            self.large_sum -= num
            self.small_sum += num
            heapq.heappush(self.small, -num)
            self.prune(self.large)

    def add(self, num):
        self.prune(self.small)

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
            self.small_sum += num
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
            self.large_sum += num

        self.balance()

    def remove(self, num):
        self.prune(self.small)
        self.prune(self.large)

        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= num
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            self.large_sum -= num
            if self.large and num == self.large[0]:
                self.prune(self.large)

        self.balance()

    def cost(self):
        self.prune(self.small)
        median = -self.small[0]

        return (
            median * self.small_size - self.small_sum
            + self.large_sum - median * self.large_size
        )


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        dh = DualHeap()

        for i in range(x):
            dh.add(nums[i])

        costs = [dh.cost()]

        for i in range(x, n):
            dh.remove(nums[i - x])
            dh.add(nums[i])
            costs.append(dh.cost())

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]