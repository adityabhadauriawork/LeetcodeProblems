class Solution:
    def isPalindrome(self, s: str) -> bool:

        

        if s == " ":
            return True
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s)
        n=len(s)
        
        l=0
        r=n-1
        for i in range(n):
            while l <= r:
                if s[l] != s[r]:
                    l+=1
                    r-=1
                    return False
                l+=1
                r-=1
            
        return True









