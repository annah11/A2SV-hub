class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        cnt = [0]*numberOfUsers
        nextO = [0]*numberOfUsers
        events.sort(key=lambda e: (int(e[1]), e[0]=="MESSAGE"))

        for typ, t, data in events:
            t = int(t)
            if typ == "OFFLINE":
                nextO[int(data)] = t + 60
                continue

            for tok in data.split():
                if tok == "ALL":
                    for u in range(numberOfUsers):
                        cnt[u] += 1
                elif tok == "HERE":
                    for u in range(numberOfUsers):
                        if t >= nextO[u]:
                            cnt[u] += 1
                else:  
                    cnt[int(tok[2:])] += 1

        return cnt