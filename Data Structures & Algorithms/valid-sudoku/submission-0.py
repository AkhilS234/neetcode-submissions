class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        map = {}
        bool = True


        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if (value != '.'):

                    val = int(value)

                    box_id = (row//3, col//3)

                    if ("row", row, val) in map:
                        bool = False 
                    else:
                        map[("row", row, val)] = True

                    if ("col", col, val) in map:
                        bool = False
                    else:
                        map[("col", col, val)] = True

                    if ("box_id", box_id, val) in map:
                        bool = False
                    else:
                        map[("box_id", box_id, val)] = True

        return bool

