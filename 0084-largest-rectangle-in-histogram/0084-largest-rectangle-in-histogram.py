class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            # maintaining increasing monotonic stack 
            while stack and heights[stack[-1]] > heights[i]:
                element_index = stack.pop()
                height = heights[element_index]
                pse = stack[-1] if stack else -1
                nse = i
                
                width = nse - pse - 1
                max_area = max(max_area, height * width)
                
            stack.append(i)
        
        while stack:
            element_index = stack.pop()
            height = heights[element_index]
            
            pse = stack[-1] if stack else -1
            nse = n 
            
            width = nse - pse - 1
            max_area = max(max_area, height * width)
            
        return max_area
