class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letter_indices = [i for i, c in enumerate(s) if c.isalpha()]
        n = len(letter_indices)
        res = []

        for mask in range(1 << n):  # 2^n combinations
            chars = list(s)
            for i in range(n):
                idx = letter_indices[i]
                if (mask >> i) & 1:
                    chars[idx] = chars[idx].upper()
                else:
                    chars[idx] = chars[idx].lower()
            res.append("".join(chars))
        
        return res