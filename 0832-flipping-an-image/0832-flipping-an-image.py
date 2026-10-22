class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        ans = []
        for row in image:
            x = row[::-1] # step 1 is done that is flip or reverse it hehe
            temp_list = []
            for a in x:
                if a == 0:
                    temp_list.append(1)
                elif a == 1:
                    temp_list.append(0)
            ans.append(temp_list)
        return ans
        