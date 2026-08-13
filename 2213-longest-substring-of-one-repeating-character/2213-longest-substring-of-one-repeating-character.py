class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        # Tree arrays to store node attributes
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.pref_char = [''] * (4 * self.n)
        self.suff_char = [''] * (4 * self.n)
        
        self.build(1, 0, self.n - 1)

    def push_up(self, node: int, left_child: int, right_child: int, l: int, r: int):
        mid = (l + r) // 2
        left_len = mid - l + 1
        right_len = r - mid

        # Inherit base properties from children
        self.pref_char[node] = self.pref_char[left_child]
        self.suff_char[node] = self.suff_char[right_child]
        self.pref_len[node] = self.pref_len[left_child]
        self.suff_len[node] = self.suff_len[right_child]
        
        # Max length is at least the max of either child
        self.max_len[node] = max(self.max_len[left_child], self.max_len[right_child])

        # If the boundaries meet with the same character, merge them
        if self.suff_char[left_child] == self.pref_char[right_child]:
            combined = self.suff_len[left_child] + self.pref_len[right_child]
            self.max_len[node] = max(self.max_len[node], combined)
            
            # If the entire left child is a single repeating character
            if self.pref_len[left_child] == left_len:
                self.pref_len[node] = left_len + self.pref_len[right_child]
                
            # If the entire right child is a single repeating character
            if self.suff_len[right_child] == right_len:
                self.suff_len[node] = right_len + self.suff_len[left_child]

    def build(self, node: int, l: int, r: int):
        if l == r:
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.pref_char[node] = self.s[l]
            self.suff_char[node] = self.s[l]
            return

        mid = (l + r) // 2
        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)
        self.push_up(node, node * 2, node * 2 + 1, l, r)

    def update(self, node: int, l: int, r: int, idx: int, char: str):
        if l == r:
            self.s[idx] = char
            self.pref_char[node] = char
            self.suff_char[node] = char
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(node * 2, l, mid, idx, char)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, char)
        self.push_up(node, node * 2, node * 2 + 1, l, r)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        tree = SegmentTree(s)
        results = []
        
        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, tree.n - 1, idx, char)
            results.append(tree.max_len[1]) # Root always tracks the overall max length
            
        return results