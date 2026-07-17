# The guess API is already defined for you.
# def guess(num: int) -> int:
#     -1 if num is higher than the picked number
#      1 if num is lower than the picked number
#      0 if num is correct

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1