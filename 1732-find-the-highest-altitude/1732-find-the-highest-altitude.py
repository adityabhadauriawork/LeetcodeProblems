class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # P[j] - P[i-1]
        # ans = []
        
        # ans.append(0)
        # for j in range(len(gain)):
        #     ans.append(ans[j] + gain[j])            

        # print(ans)    
        
        final_ans = 0
        max_alt = 0
        for a in gain:
            max_alt += a
            final_ans = max(final_ans, max_alt)
        return final_ans



        