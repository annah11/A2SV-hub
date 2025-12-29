class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        rec = defaultdict(list)
        for x in allowed:
            rec[x[:2]].append(x[2])

        def dfs(bottom):
            if len(bottom) == 1:
                return True
            for b in product(*(rec[x + y] for x, y in zip(bottom[:-1], bottom[1:]))):
                if dfs(b):
                    return True
            return False

        return dfs(bottom)