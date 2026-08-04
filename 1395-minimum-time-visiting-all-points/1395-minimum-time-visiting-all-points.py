class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if points == []:
            return 0
        x1, y1 = points.pop()
        time = 0
        while points != []:             
            x2, y2 = points.pop()
            time += max((abs(y2 - y1)), abs(x2 - x1))
            x1, y1 = x2, y2
        return time