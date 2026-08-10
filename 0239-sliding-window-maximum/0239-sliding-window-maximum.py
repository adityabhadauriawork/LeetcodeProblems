from collections import deque

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        
        for i in range(k):
            while queue and arr[queue[-1]] <= arr[i]:
                queue.pop()
            queue.append(i)
            
        ans.append(arr[queue[0]])
        
        for i in range(k, len(arr)):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and arr[queue[-1]] <= arr[i]:
                queue.pop()
            queue.append(i)
            ans.append(arr[queue[0]])
            
        return ans
