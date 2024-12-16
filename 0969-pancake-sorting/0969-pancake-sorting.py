class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n= len(arr)
        res =[]
        def flip(arr,k):
            arr[:k]=arr[:k][::-1]
        
        for size in range(n, 1, -1):
            max_index = arr.index(max(arr[:size]))
            if max_index != size - 1:
                if max_index != 0:
                    flip(arr, max_index + 1)
                    res.append(max_index+1)
                flip(arr, size)
                res.append(size)
        
        return res