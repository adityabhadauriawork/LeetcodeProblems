class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # P[j] - P[i-1]
        ans = []
        
        ans.append(0)
        for j in range(len(gain)):
            ans.append(ans[j] + gain[j])            

        print(ans)    
        return max(ans)


        