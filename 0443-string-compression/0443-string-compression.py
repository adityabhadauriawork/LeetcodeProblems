class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0
        while i < len(chars):
            group = 1
            while (i + group) < len(chars) and chars[i+group]==chars[i]:
                group +=1
            chars[insert] = chars[i]
            insert+=1
            # Write the count if greater than 1
            if group > 1:
                string = str(group)
                chars[insert:insert+len(string)] = list(string)
                insert += len(string)
            i += group
        return insert