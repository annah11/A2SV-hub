class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rmCnt = [0] * value

        for num in nums:
            rem = ((num % value) + value) % value
            rmCnt[rem] += 1

        hin = 0
        while rmCnt[hin % value] > 0:
            rmCnt[hin % value] -= 1
            hin += 1

        return hin