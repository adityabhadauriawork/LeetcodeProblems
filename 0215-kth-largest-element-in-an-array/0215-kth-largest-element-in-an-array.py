import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        h = []
        for a in nums:
            heapq.heappush(h,a)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]
        