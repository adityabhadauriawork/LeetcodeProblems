import heapq
import bisect

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to store (end_time, server_id) for busy servers
        busy = []
        # Sorted list of available server IDs
        available = list(range(k))
        # Keep track of counts for each server
        counts = [0] * k
        
        for i, (arr_time, load_time) in enumerate(zip(arrival, load)):
            # Free up servers whose tasks finish <= current arrival time
            while busy and busy[0][0] <= arr_time:
                _, freed_server = heapq.heappop(busy)
                bisect.insort(available, freed_server)
            
            if not available:
                # All servers are busy; drop the request
                continue
            
            # Find the preferred server index: i % k
            pref = i % k
            idx = bisect.bisect_left(available, pref)
            
            if idx == len(available):
                # Wrap around to the beginning of the available list
                server_id = available.pop(0)
            else:
                server_id = available.pop(idx)
            
            counts[server_id] += 1
            heapq.heappush(busy, (arr_time + load_time, server_id))
        
        max_requests = max(counts) if counts else 0
        return [i for i, c in enumerate(counts) if c == max_requests]
