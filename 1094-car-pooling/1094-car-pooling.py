class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for i in range(len(trips)):
            if trips[i][0]+trips[i-1][0] > capacity:
                if trips[i][2] > trips[i-1][1]:
                    return False
            return True