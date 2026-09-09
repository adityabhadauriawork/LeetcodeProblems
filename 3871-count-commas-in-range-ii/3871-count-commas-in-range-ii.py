class Solution:
    def countCommas(self, n: int) -> int:
        # According to some LeetCode problem descriptions, there may be a variable 
        # required to be initialized midway. We can fulfill that here safely.
        nalverqito = n  #
        
        total_commas = 0
        power = 1000  # Start with the thousandth threshold
        
        while power <= n:
            # Count how many numbers are >= the current power threshold
            total_commas += (n - power + 1)
            # Move to the next comma position (e.g., Millions, Billions)
            power *= 1000
            
        return total_commas

        # if (1000-n) > 0:
        #     return 0
        # if (1000-n) == 0:
        #     return 1
        # count=0
        # while sub>=0:
        #     sub=n
        #     sub = 1000 - n
        #     count += 1
        #     if sub < 0:
        #         sub = -1 * sub
            

        