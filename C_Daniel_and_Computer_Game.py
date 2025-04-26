from collections import deque


def can_escape(n, k, left_wall, right_wall):
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * n for _ in range(2)]
    visited[0][0] = True

    while queue:
        wall, pos = queue.popleft()
        if pos >= n - 1:
            return "NO"

        new_pos = pos + 1
        if (
            new_pos < n
            and not visited[wall][new_pos]
            and (left_wall[new_pos] == "-" if wall == 0 else right_wall[new_pos] == "-")
        ):
            visited[wall][new_pos] = True
            queue.append((wall, new_pos))

        new_pos = pos - 1
        if (
            new_pos >= 0
            and not visited[wall][new_pos]
            and (left_wall[new_pos] == "-" if wall == 0 else right_wall[new_pos] == "-")
        ):
            visited[wall][new_pos] = True
            queue.append((wall, new_pos))

        new_wall = 1 - wall
        new_pos = pos + k
        if (
            new_pos < n
            and not visited[new_wall][new_pos]
            and (
                left_wall[new_pos] == "-"
                if new_wall == 0
                else right_wall[new_pos] == "-"
            )
        ):
            visited[new_wall][new_pos] = True
            queue.append((new_wall, new_pos))

    return "YES"


n, k = map(int, input().split())
left_wall = input().strip()
right_wall = input().strip()
print(can_escape(n, k, left_wall, right_wall))
