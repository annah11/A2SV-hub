class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        c = Counter()
        top = SortedList()
        rest = SortedList()
        sumTop = 0
        res = []

        def add(num):
            nonlocal sumTop
            old = c[num]
            if old > 0:
                tup = (-old, -num)
                if tup in top:
                    top.remove(tup)
                    sumTop -= old * num
                else:
                    rest.remove(tup)
            c[num] += 1
            tup = (-c[num], -num)
            rest.add(tup)
            rebalance()

        def remove(num):
            nonlocal sumTop
            old = c[num]
            tup = (-old, -num)
            if tup in top:
                top.remove(tup)
                sumTop -= old * num
            else:
                rest.remove(tup)
            c[num] -= 1
            if c[num] == 0:
                del c[num]
            else:
                tup = (-c[num], -num)
                rest.add(tup)
            rebalance()

        def rebalance():
            nonlocal sumTop
            while len(top) < x and rest:
                t = rest.pop(0)
                top.add(t)
                f, n = t
                sumTop += (-f) * (-n)
            while len(top) > x:
                t = top.pop()
                f, n = t
                sumTop -= (-f) * (-n)
                rest.add(t)
            # Maintain order if rest[0] > top[-1]
            while rest and top and rest[0] < top[-1]:
                low = top.pop()
                high = rest.pop(0)
                f1, n1 = low
                f2, n2 = high
                sumTop -= (-f1) * (-n1)
                sumTop += (-f2) * (-n2)
                top.add(high)
                rest.add(low)

        for i, num in enumerate(nums):
            add(num)
            if i >= k:
                remove(nums[i - k])
            if i >= k - 1:
                res.append(sumTop)

        return res