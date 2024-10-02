class Solution:
    def printVertically(self, s: str) -> List[str]:  # noqa: F821
        words = s.split()
        
        max_len = max(len(word) for word in words)
        
        result = []
        
        for i in range(max_len):
            current_row = []
            for word in words:
                if i < len(word):
                    current_row.append(word[i])
                else:
                    current_row.append(" ")
            result.append("".join(current_row).rstrip())
        
        return result
