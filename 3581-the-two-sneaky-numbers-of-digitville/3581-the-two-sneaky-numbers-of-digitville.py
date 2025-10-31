class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hin = []
        cnt = Counter(nums)
        # print(cnt)
        for i,v in cnt.items():
            if v> 1:
                hin.append(i)
        return hin
