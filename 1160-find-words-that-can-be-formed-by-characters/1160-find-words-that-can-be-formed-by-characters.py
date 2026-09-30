class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        from collections import Counter
        chars_count = Counter(chars)
        res = 0
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= chars_count[c] for c in word_count):
                res += len(word)
        return res
