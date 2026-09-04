class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        ans = []
        for i, word in enumerate(sentence.split(), 1):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            ans.append(word + "ma" + "a" * i)
        return " ".join(ans)