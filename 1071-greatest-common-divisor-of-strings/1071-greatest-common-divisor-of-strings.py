import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        l1=len(str1)
        l2=len(str2)
        gcd1=math.gcd(l1,l2)
        if l1>l2:
            return str1[:gcd1]
        else:
            return str2[:gcd1]

        