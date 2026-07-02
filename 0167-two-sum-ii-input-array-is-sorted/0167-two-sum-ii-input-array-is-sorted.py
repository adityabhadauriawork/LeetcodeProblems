class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # freq = {}
        # for i in range(len(numbers)):
        #     current_number = numbers[i]
        #     req_no = target - current_number
        #     if req_no in freq:
        #         return freq[req_no]+1, i+1
        #     else:
        #         freq[current_number] = i

        # two pointer approach
        # l = 0
        # r = len(numbers)-1
        # while l<r:
        #     sum1 = numbers[l]+numbers[r]
        #     if sum1 == target:
        #         return [l+1,r+1]
        #     elif sum1<target:
        #         l+=1
        #     else:
        #         r-=1
        n = len(nums)
        r = n -1
        l = 0
        while l <= r:
            if nums[l] + nums[r] == target:
                return [l+1, r+1]
            elif nums[l] + nums[r] > target:
                r-=1
            else:
                l+=1
        

        




        
        