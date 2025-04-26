# FINAL VERSION OF THE CODE

import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    n, m, k = [int(i) for i in input().split()]

    mat = []

    for _ in range(n):
        mat.append(list(input()))

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def inbound(r, c):
        return 0 <= r < n and 0 <= c < m

    def border(r, c):
        return (r == 0) or (r == n - 1) or (c == 0) or (c == m - 1)

    def dfs(row, col):
        nonlocal is_lake
        nonlocal lake
        visited.add((row, col))

        if border(row, col):
            is_lake = False

        lake.append((row, col))

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if inbound(nr, nc) and (nr, nc) not in visited and mat[nr][nc] == ".":
                dfs(nr, nc)

    Lakes = []
    visited = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "." and (i, j) not in visited:
                lake = []
                is_lake = True
                dfs(i, j)

                if is_lake:
                    Lakes.append((len(lake), lake))

    Lakes.sort()

    rem = len(Lakes) - k

    cnt = 0
    for i in range(rem):
        lake = Lakes[i]
        cnt += lake[0]
        for r, c in lake[1]:
            mat[r][c] = "*"

    print(cnt)
    for row in mat:
        print("".join(row))


if __name__ == "__main__":
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
