class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        curr_sum, count = 0, 0
        for num in arr:
            curr_sum += num
            if curr_sum == target:
                count += 1
                curr_sum = 0
                if count == 3:
                    return True
        return False
