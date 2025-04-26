r1, c1, r2, c2 = map(int, input().split())


# bishop = (-1, -1), (-1, 1), (1, -1), (1, 1)
# knight = (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)
# rook = (-1, 0), (1, 0), (0, -1), (0, 1)
def rook(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2:
        return 1
    else:
        return 2


def bishop(r1, c1, r2, c2):
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        return 0
    elif abs(r1 - r2) == abs(c1 - c2):
        return 1
    else:
        return 2


def king(r1, c1, r2, c2):
    return max(abs(r1 - r2), abs(c1 - c2))


rook_moves = rook(r1, c1, r2, c2)
bishop_moves = bishop(r1, c1, r2, c2)
king_moves = king(r1, c1, r2, c2)
print(rook_moves, bishop_moves, king_moves)
