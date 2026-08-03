class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices) == 1:
            return prices
        stack = []
        
        for i in range(len(prices)):
            flag = False
            for j in range(i+1, len(prices)):
                
                if prices[j] <= prices[i]:
                    stack.append(prices[i] - prices[j])
                    flag = True
                    break
                elif prices[j] > prices[i]:
                    continue
            if flag == False:
                stack.append(prices[i])
        return stack
                

        