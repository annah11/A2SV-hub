# Directions: D < L < R < U
# Down = 'D' (1, 0), Left = 'L' (0, -1), Right = 'R' (0, 1), Up = 'U' (-1, 0)
directions = [("D", 1, 0), ("L", 0, -1), ("R", 0, 1), ("U", -1, 0)]


def solve(n, m, k, maze):
    # Find the starting position 'X'
    start_x, start_y = -1, -1
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "X":
                start_x, start_y = i, j
                break
        if start_x != -1:
            break

    # To store the visited positions with the current path
    visited = set()

    # We need to backtrack through possible paths
    def dfs(x, y, path, steps):
        # If we have already reached k steps and are back at the starting point
        if steps == k:
            if (x, y) == (start_x, start_y):
                return path
            return None

        # Try every direction in lexicographical order
        for direction, dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maze[nx][ny] != "*"
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                result = dfs(nx, ny, path + direction, steps + 1)
                if result:
                    return result
                visited.remove((nx, ny))
        return None

    # Start DFS from the starting point
    visited.add((start_x, start_y))
    result = dfs(start_x, start_y, "", 0)
    return result if result else "IMPOSSIBLE"


# Input parsing
n, m, k = map(int, input().split())
maze = [input().strip() for _ in range(n)]

# Solve the problem and print the result
print(solve(n, m, k, maze))
