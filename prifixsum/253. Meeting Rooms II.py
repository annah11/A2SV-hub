def meetingRoom(intervals):
    intervals.sort(key=lambda x:x[0]x[1])
    max_room =0
    res = []
    for i in intervals:
        res.append(i.start,1)
        res.append(i.end,0)
    res.sort()
    ans = 0
    for room in res:
        if room[i] ==1:
    