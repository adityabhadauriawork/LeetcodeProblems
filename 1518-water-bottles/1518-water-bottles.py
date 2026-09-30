class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            new_bottles, rem = divmod(numBottles, numExchange)
            ans += new_bottles
            numBottles = new_bottles + rem
        return ans
