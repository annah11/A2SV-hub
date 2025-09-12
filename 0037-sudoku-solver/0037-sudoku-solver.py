class Solution:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    d = int(ch)
                    bit = 1 << (d - 1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box_id(r, c)] |= bit

        def popcount(x):
            return bin(x).count("1")   

        ALL = (1 << 9) - 1

        def solve():
            if not empties:
                return True

            best_i = -1
            best_mask = 0
            best_cnt = 10

            for i, (r, c) in enumerate(empties):
                mask = ALL ^ (rows[r] | cols[c] | boxes[box_id(r, c)])
                cnt = popcount(mask)
                if cnt == 0:
                    return False
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_mask = mask
                    best_i = i
                    if cnt == 1:
                        break

            r, c = empties.pop(best_i)
            b = box_id(r, c)
            mask = best_mask

            while mask:
                bit = mask & -mask
                d = (bit.bit_length() - 1) + 1
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                board[r][c] = str(d)

                if solve():
                    return True

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = '.'

                mask ^= bit

            empties.insert(best_i, (r, c))
            return False

        solve()
