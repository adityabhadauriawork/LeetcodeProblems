from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        lis = []
        ans = []

        for x in obstacles:
            idx = bisect_right(lis, x)

            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x

            ans.append(idx + 1)

        return ans