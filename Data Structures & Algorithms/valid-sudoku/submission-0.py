class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap, rcMap = defaultdict(set), defaultdict(set), defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                
                if num in rowMap[row] or num in colMap[col] or num in rcMap[(row//3, col//3)]:
                    return False
                
                rowMap[row].add(num)
                colMap[col].add(num)
                rcMap[(row//3, col//3)].add(num)
        
        return True
                