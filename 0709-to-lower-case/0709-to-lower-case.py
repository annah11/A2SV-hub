class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for char in s:
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return ''.join(result)
