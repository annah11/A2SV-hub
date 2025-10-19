class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = deque([s])
        visited = set()
        smallest = s
        while queue:
            string = queue.popleft()
            if string in visited:
                continue
            visited.add(string)
            
            chars = list(string)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            new_string = "".join(chars)
            queue.append(new_string)
            rotated_string = string[-b:] + string[:-b]
            queue.append(rotated_string)

            if string < smallest:
                smallest = string
        
        return smallest


    
        