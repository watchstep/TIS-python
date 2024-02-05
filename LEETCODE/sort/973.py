# 973. K Closest Points to Origin

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def get_dist(point):
            return point[0] ** 2 + point[1] ** 2
        dists = [get_dist(p) for p in points]
        res = list(zip(points, dists))
        res.sort(key=lambda x:x[1])
        return [p for (p, d) in res[:k]]

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        from heapq import heappush, heappop
        
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heappush(heap, (dist, x, y))
        
        res = []
        for _ in range(k):
            dist, x, y = heappop(heap)
            res.append((x, y))
        return res
            