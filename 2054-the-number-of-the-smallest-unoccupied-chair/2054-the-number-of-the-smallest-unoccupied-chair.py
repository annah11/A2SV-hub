class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        heap = []
        arr =[]
        dic = defaultdict(int)
        for i in range(len(times)):
            arr.append((times[i][0],1,i))
            arr.append((times[i][1],0,i))
        arr.sort()
        print(arr)
        chair = list(range(len(times)))
        heapify(chair)
        for j,stat,fr in arr:
            if stat == 0:
                heappush(chair,dic[fr])
            else:
                dic[fr]=heappop(chair)
        print(dic)
        return dic[targetFriend]