class Solution:
    def validStrings(self, n: int) -> List[str]:
        def back(idx, cur):
            if idx == n:
                return [cur]
            res = []
            if cur and cur[-1] == "0":
                res += back(idx + 1, cur + "1")
            else:
                res += back(idx + 1, cur + "0")
                res += back(idx + 1, cur + "1")

            return res

        return back(0, "")