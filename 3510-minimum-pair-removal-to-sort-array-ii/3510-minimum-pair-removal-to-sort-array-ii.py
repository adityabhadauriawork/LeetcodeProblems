class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        val = list(nums)
        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 if i + 1 < n else -1 for i in range(n)]
        removed = [False] * n
        
        bad = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                bad += 1
                
        if bad == 0:
            return 0
            
        pq = [(val[i] + val[i + 1], i) for i in range(n - 1)]
        heapq.heapify(pq)
        ops = 0
        
        while bad > 0 and pq:
            s, i = heapq.heappop(pq)
            j = nxt[i]
            if removed[i] or j == -1 or removed[j] or val[i] + val[j] != s:
                continue
                
            p = prev[i]
            nn = nxt[j]
            
            if p != -1 and val[p] > val[i]:
                bad -= 1
            if val[i] > val[j]:
                bad -= 1
            if nn != -1 and val[j] > val[nn]:
                bad -= 1
                
            val[i] = s
            removed[j] = True
            nxt[i] = nn
            if nn != -1:
                prev[nn] = i
                
            if p != -1 and val[p] > val[i]:
                bad += 1
            if nn != -1 and val[i] > val[nn]:
                bad += 1
                
            if p != -1:
                heapq.heappush(pq, (val[p] + val[i], p))
            if nn != -1:
                heapq.heappush(pq, (val[i] + val[nn], i))
                
            ops += 1
            
        return ops