class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = []
        for i in range(n):
            adjList.append([])
        for edge in times:
            x = edge[0]-1
            y = edge[1]-1
            w = edge[2]
            adjList[x].append([y,w])
            # ajdList[y].append([x,w])

        heap=[]
        dist = [float("inf")]*n
        k-=1
        dist[k]=0
        heappush(heap,(dist[k],k))

        while len(heap) > 0:
            d,u= heappop(heap)
            for v,w in adjList[u]:
                if dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
                    heappush(heap,(dist[v],v))
        ans = max(dist)
        if ans==float("inf"):
            return -1
        return ans


        
        