from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert both lists to sets (hash tables internally)
        set1, set2 = set(nums1), set(nums2)
        
        # Elements in set1 but not in set2
        diff1 = list(set1 - set2)
        
        # Elements in set2 but not in set1
        diff2 = list(set2 - set1)
        
        return [diff1, diff2]
