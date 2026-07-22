from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events):
        events.sort()

        starts = [x[0] for x in events]

        suffix = [0] * len(events)

        suffix[-1] = events[-1][2]

        for i in range(len(events) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], events[i][2])

        ans = 0

        for s, e, v in events:
            idx = bisect_right(starts, e)
            ans = max(ans, v)

            if idx < len(events):
                ans = max(ans, v + suffix[idx])

        return ans