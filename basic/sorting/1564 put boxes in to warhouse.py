def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
    n = len(warehouse)
    left = warehouse[0]*n
    boxes.sort()
    for i in range(n):
        left = min(left[i-1] ,warehouse[i])
        i,j = 0 ,n-1
        while i<=j :
            i+=1
            j-=1
            