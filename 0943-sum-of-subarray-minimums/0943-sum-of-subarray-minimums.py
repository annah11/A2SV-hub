class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        res, n = 0, len(arr)

        for i in range(n + 1):
            while stack and (i == n or arr[i] < arr[stack[-1]]):
                j = stack.pop()
                left = j - (stack[-1] if stack else -1)
                right = i - j
                res = (res + arr[j] * left * right) % MOD
            stack.append(i)

        return res