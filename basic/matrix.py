class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # noqa: F821
        res = defaultdict(list)  # noqa: F821
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())