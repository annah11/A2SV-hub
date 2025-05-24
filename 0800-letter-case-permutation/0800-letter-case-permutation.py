class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        for ch in s:
            if ch.isalpha():
                result = [res + c for res in result for c in [ch.lower(), ch.upper()]]
            else:
                result = [res + ch for res in result]
        return result
