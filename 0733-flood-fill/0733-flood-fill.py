class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        initally =image[sr][sc]
        if color == initally:
            return image
        q = deque()
        q.append((sr,sc))
        while q:
            i,j = q.popleft()
            if i <0 or i>=m or j<0 or j >= n or image[i][j] !=initally:
                continue
             
            image[i][j] = color
            q.append((i-1,j))
            q.append((i+1,j))
            q.append((i,j-1))
            q.append((i,j+1))
        return image