class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
 
      
        for row in board:
            nums = [num for num in row if num != '.']
            if len(nums) != len(set(nums)):
                return False

    
        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != '.']
            if len(nums) != len(set(nums)):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = [board[x][y] for x in range(i, i+3) for y in range(j, j+3) if board[x][y] != '.']
                if len(nums) != len(set(nums)):
                    return False

        return True