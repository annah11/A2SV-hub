class NumArray:

    def __init__(self, nums: List[int]):
        self._sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self._sum[i+1] = self._sum[i] +nums[i]
        print(self._sum)

        

    def sumRange(self, left: int, right: int) -> int:
        return self._sum[right+1] - self._sum[left]

            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)