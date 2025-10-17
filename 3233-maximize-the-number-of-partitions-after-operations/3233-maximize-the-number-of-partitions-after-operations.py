class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dp(i, seen, can_change):
            if i == n: return 1
            
            char_bit = 1 << (ord(s[i]) - ord('a'))
            distinct = seen.bit_count()
            
            if char_bit & seen:
                res = dp(i + 1, seen, can_change)
            elif distinct < k:
                res = dp(i + 1, seen | char_bit, can_change)
            else:
                res = 1 + dp(i + 1, char_bit, can_change)
            
            keep_seen = seen | char_bit
            if can_change:
                for c in range(26):
                    new_bit = 1 << c
                    if new_bit & keep_seen: 
                        continue
                    elif distinct < k:
                        res = max(res, dp(i + 1, seen | new_bit, 0))
                    else:
                        res = max(res, 1 + dp(i + 1, new_bit, 0))
            
            return res
        
        n = len(s)
        return dp(0, 0, 1)