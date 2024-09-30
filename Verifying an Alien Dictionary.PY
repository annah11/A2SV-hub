class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:  # noqa: F821
    
        order_map = {char: i for i, char in enumerate(order)}
        
        def is_sorted(word1, word2):
            for c1, c2 in zip(word1, word2):
                if order_map[c1] < order_map[c2]:
                    return True
                elif order_map[c1] > order_map[c2]:
                    return False
            return len(word1) <= len(word2)
        
        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False
        
        return True
