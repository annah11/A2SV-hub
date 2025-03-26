class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = []
        for i in range(len(matrix)):
            ans. extend(matrix[i])
        print(ans)
        left,right= 0 ,len(ans)-1
        while left <= right:
            mid = (left +right)//2
            if ans[mid]>target:
                right =mid -1
            elif ans[mid] < target:
                left = mid +1
            else:
                return True
        return False