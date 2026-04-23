class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for i in range(0 , len(nums) , 1):
            if nums[i] == target:
                return i
        else:
            return -1

    