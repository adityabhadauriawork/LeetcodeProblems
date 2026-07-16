from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # Find sorted prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # Already sorted
        if left == n - 1:
            return 0

        # Find sorted suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Remove only prefix or only suffix
        ans = min(right, n - left - 1)

        i = 0
        j = right

        while i <= left and j < n:

            if arr[i] <= arr[j]:
                # Remove everything between i and j
                ans = min(ans, j - i - 1)
                i += 1
            else:
                # Need a bigger element on the right
                j += 1

        return ans