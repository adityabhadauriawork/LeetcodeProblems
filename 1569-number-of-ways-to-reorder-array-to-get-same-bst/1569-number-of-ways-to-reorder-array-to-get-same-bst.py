class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        from math import comb


        MOD = 10**9 + 7
        
        def ways(arr: list[int]) -> int:
            # Base case: if array has 2 or fewer elements, there is only 1 valid configuration
            if len(arr) <= 2:
                return 1
            
            # The first element is always the root
            root = arr[0]
            
            # Split the remaining elements into left and right subtrees
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            # Total ways to interleave left and right elements is comb(len(left) + len(right), len(left))
            return (comb(len(left) + len(right), len(left)) * ways(left) * ways(right)) % MOD
            
        # Subtract 1 to exclude the original array ordering itself
        return (ways(nums) - 1) % MOD

        