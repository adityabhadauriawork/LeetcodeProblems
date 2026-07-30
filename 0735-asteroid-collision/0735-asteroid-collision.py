class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stk = []

        for i in range(len(nums)):

            if nums[i] > 0:
                stk.append(nums[i])
                continue

            while stk and stk[-1] > 0 and abs(nums[i]) > abs(stk[-1]):
                stk.pop()

            if not stk or stk[-1] < 0:
                stk.append(nums[i])
                continue

            if abs(nums[i]) == abs(stk[-1]):
                stk.pop()
                continue

            # if stk[-1] > abs(nums[i]), do nothing
            # the current asteroid is destroyed

        return stk