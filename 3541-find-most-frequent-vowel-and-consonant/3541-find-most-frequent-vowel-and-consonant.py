class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}
        count_vowel = 0
        count_cons = 0
        vowel = set("aeiou")
        for a in s:
            if a in freq:
                freq[a] += 1
            else:
                freq[a] = 1
        for letter, count in freq.items():
            if letter in vowel:
                if count > count_vowel:
                    count_vowel = count
            elif letter not in vowel:
                if count > count_cons:
                    count_cons = count
        return count_cons + count_vowel



                

