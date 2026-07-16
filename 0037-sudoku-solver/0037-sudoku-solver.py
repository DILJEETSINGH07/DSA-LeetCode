from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        boxes = [[False] * 10 for _ in range(9)]

        # Store existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i][num] = True
                    cols[j][num] = True
                    boxes[(i // 3) * 3 + (j // 3)][num] = True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        box = (i // 3) * 3 + (j // 3)

                        for num in range(1, 10):
                            if not rows[i][num] and not cols[j][num] and not boxes[box][num]:
                                board[i][j] = str(num)
                                rows[i][num] = True
                                cols[j][num] = True
                                boxes[box][num] = True

                                if backtrack():
                                    return True

                                board[i][j] = "."
                                rows[i][num] = False
                                cols[j][num] = False
                                boxes[box][num] = False

                        return False
            return True

        backtrack()