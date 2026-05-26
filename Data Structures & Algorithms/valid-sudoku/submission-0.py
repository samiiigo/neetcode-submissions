class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for col in board:
            seen = set()
            for i in col:
                if i == ".": continue
                if i in seen: return False
                seen.add(i)
            
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[i][row] == ".": continue
                if board[i][row] in seen: return False
                seen.add(board[i][row])
            
        for block in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (block//3) * 3 + i
                    col = (block % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True