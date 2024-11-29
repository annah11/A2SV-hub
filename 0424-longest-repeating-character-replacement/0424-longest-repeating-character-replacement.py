class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        freq = defaultdict(int)
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_count = max(max_count, freq[s[r]])
            if (r - l + 1) - max_count > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
