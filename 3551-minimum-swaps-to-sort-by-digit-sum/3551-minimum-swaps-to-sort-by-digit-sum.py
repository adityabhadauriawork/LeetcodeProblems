# from typing import List

# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
            # tle wala code hai biro
        # def digit_sum(num):
        #     return sum(map(int, str(num)))

        # target = sorted(nums, key=lambda x: (digit_sum(x), x))

        # arr1 = nums.copy()
        # swap = 0

        # for i in range(len(arr1)):
        #     if arr1[i] != target[i]:
        #         j = arr1.index(target[i])

        #         arr1[i], arr1[j] = arr1[j], arr1[i]
        #         swap += 1

        # return swap

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(num):
            return sum(map(int, str(num)))

        target = sorted(nums, key=lambda x: (digit_sum(x), x))

        arr = nums.copy()
        pos = {num: i for i, num in enumerate(arr)}
        swaps = 0

        for i in range(len(arr)):
            if arr[i] != target[i]:
                correct = target[i]
                j = pos[correct]
                current = arr[i]

                arr[i], arr[j] = arr[j], arr[i]

                pos[correct] = i
                pos[current] = j

                swaps += 1

        return swaps