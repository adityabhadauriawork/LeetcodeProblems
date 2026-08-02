class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        freq = {}

        # value -> index
        for i in range(len(nums2)):
            freq[nums2[i]] = i

        stack = []

        for i in range(len(nums1)):
            count = 0

            for j in range(freq[nums1[i]] + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    stack.append(nums2[j])
                    break
                else:
                    count += 1

            if count == len(nums2) - (freq[nums1[i]] + 1):
                stack.append(-1)

        return stack