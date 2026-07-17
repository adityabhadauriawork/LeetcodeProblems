from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        ans = []
        prefix = ""

        for ch in searchWord:
            prefix += ch

            idx = bisect.bisect_left(products, prefix)

            suggestion = []

            for i in range(idx, min(idx + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestion.append(products[i])

            ans.append(suggestion)

        return ans