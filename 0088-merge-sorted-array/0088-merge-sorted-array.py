class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        k = m+n-1
        while j>=0:
            if  i<0 or nums2[j] > nums1[i]:
                nums1[k]=nums2[j]
                k-=1
                j-=1
                #if they nums 1 ka i equal hai nums2 ke j se to else chle !!
            else:
                nums1[k]=nums1[i]
                k-=1
                i-=1



        """
        Do not return anything, modify nums1 in-place instead.
        """
        