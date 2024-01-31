# 743. Network Delay Time
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        from heapq import heappush, heappop
        
        time_list = [int(1e9)*(n + 1)]
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
            
        def dijkstra(k):
            heap = []
            heappush(heap, (0, k))
            time_list[k] = 0
            while heap:
                time, curr = heappop(heap)
                if time_list[curr] < time:
                    continue
                for next_node, weight in graph[curr]:
                    cost = time + weight
                    time_list[next_node] = cost
                    heappush(heap, (cost, next_node))
        dijkstra()
                