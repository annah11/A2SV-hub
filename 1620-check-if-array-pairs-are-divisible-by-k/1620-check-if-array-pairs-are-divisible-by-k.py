class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = Counter()
        for i in arr:
            cnt[i % k] += 1
        if 0 in cnt:
            if cnt[0] % 2 != 0:
                return False
        del cnt[0]
        for r in cnt:
            if cnt[r] != cnt[k-r]:
                return False
        return True