class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even=0
        odd=0
        for i in range(1, len(nums1)):
            if (nums1[i-1]-nums1[i]) % 2 == 0:
                if nums1[i] %2 == 0:
                    even += 1
            if (nums1[i-1]-nums1[i]) % 2 != 0:
                if nums1[i] %2 != 0:
                    odd += 1
        if even == len(nums1) or odd == len(nums1):
            return False
        return True

        