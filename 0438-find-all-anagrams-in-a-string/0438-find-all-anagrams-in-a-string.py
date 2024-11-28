class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter()
        result = []
        k = len(p)
        for i in range(len(s)):
            s_count[s[i]] += 1
            if i >= k:
                if s_count[s[i - k]] == 1:
                    del s_count[s[i - k]]
                else:
                    s_count[s[i - k]] -= 1
            if s_count == p_count:
                result.append(i - k + 1)
        print(p_count)
        print(s_count)
        return result
