class Solution:
    def reverseVowels(self, s: str) -> str:

        # vowel_ind = []
        # vowel_char = []

        # for i in range(len(s)):
        #     if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
        #         vowel_ind.append(i)
        #         vowel_char.append(s[i])

        # vowel_char = vowel_char[::-1]

        # new_string = list(s)

        # for i in range(len(vowel_ind)):
        #     new_string[vowel_ind[i]] = vowel_char[i]

        # return "".join(new_string)

        # SECOND APPROAC TWO POINTER
        a = set("aeiouAEIOU")
        s=list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and s[left] not in a:
                left+=1
            while left < right and s[right] not in a:
                right -=1
            s[left] , s[right] = s[right] , s[left]
            left+=1
            right-=1
        return "".join(s)



