class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n1 = len(nums2)

        for i in range(len(nums1)):
            count = 0

            # Find the position of nums1[i] in nums2
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    break

            # Search only to the right
            for k in range(j + 1, len(nums2)):
                if nums2[k] > nums1[i]:
                    stack.append(nums2[k])
                    break
                else:
                    count += 1

            if count == len(nums2) - (j + 1):
                stack.append(-1)

        return stack