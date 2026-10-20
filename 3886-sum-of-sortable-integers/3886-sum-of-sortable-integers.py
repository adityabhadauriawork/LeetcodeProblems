# TLE WALA CODE BUT WORKING HAI
# class Solution:
#     def divisors(self, nums):
#         div = []
#         for num in range(1, len(nums) + 1):
#             if len(nums) % num == 0:
#                 div.append(num)
#         return div

#     def sortableIntegers(self, nums: list[int]) -> int:
#         k = self.divisors(nums)
#         addition = 0
#         target = sorted(nums)

#         for divv in k:
#             result = []

#             for i in range(0, len(nums), divv):
#                 group = nums[i:i + divv]   # [0:0 + 3] = [0:3] okay

#                 if not self.can_rotate(group):
#                     break

#                 result.extend(sorted(group))

#             if result == target:
#                 addition += divv

#         return addition

#     def can_rotate(self, group):
#         target = sorted(group)

#         for i in range(len(group)):
#             rotated = group[i:] + group[:i]

#             if rotated == target:
#                 return True

#         return False


class Solution:
    def divisors(self, nums):
        div = []
        for num in range(1, len(nums) + 1):
            if len(nums) % num == 0:
                div.append(num)
        return div

    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        addition = 0

        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1]
            if nums[i - 1] > nums[i]:
                pref_drop[i] += 1

        for divv in self.divisors(nums):
            possible = True

            for i in range(0, n, divv):
                end = i + divv - 1

                drops = pref_drop[end] - pref_drop[i]

                if nums[end] > nums[i]:
                    drops += 1

                if drops > 1 or pref_max[i] > suff_min[i]:
                    possible = False
                    break

            if possible:
                addition += divv

        return addition
