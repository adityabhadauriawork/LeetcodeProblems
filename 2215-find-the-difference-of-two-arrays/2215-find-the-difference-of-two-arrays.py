class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # freq1 = {}

        # for a in nums1:
        #     if a in freq1:
        #         freq1[a]+=1
        #     else:
        #         freq1[a]=1
        # for b in nums2:
        #     if b not in freq1:

        
        # ans=[]
        # if freq1.values() not in freq2.values():
        #     ans.append([freq1.values()])
        # if freq2.values() not in freq1.values():
        #     ans.append([freq2.values()])
        # return ans
        ans1 = []
        
        ans3=[]
        for a in nums1:
            if a not in nums2:
                ans1.append(a)
        ans1=set(ans1)
        ans1=list(ans1)
        ans2=[]
        for b in nums2:
            if b not in nums1:
                ans2.append(b)
        ans2=set(ans2)
        ans2=list(ans2)
        ans3.append(ans1)

        ans3.append(ans2)
        return ans3






        
        