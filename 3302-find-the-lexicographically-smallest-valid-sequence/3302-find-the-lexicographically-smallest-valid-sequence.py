class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # Store the last possible index in word1 for each character in word2
        last_idx = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last_idx[j] = i
                j -= 1

        # Find the lexicographically smallest sequence
        result = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            # Match found without using the modification
            if word1[i] == word2[j]:
                result.append(i)
                j += 1

            # Use the one allowed modification
            else:
                if not changed and (j == m - 1 or last_idx[j + 1] > i):
                    result.append(i)
                    j += 1
                    changed = True

        return result if len(result) == m else []