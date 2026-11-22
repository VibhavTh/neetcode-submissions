class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         
        #we need to track rows, cols, and squares to make sure a board is valid
        #use a hashset to check for duplicates and have fast O(1) lookup
        #using a lot of memory but having fast time due to nature of problem and data structures we're using
        #we can also consider the squares as a 3 x 3 matrix and calculate the index of a square using ((row // 3) * 3 + (col // 3) if we're counting left to right row by row

        # 0 1 2 - 0
        # 3 4 5 - 1
        # 6 7 8 - 2


        #1, 1 -  square 

    
        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # squares = [set() for _ in range(9)]

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] != ".":
        #             val = int(board[i][j])
        #             squares_index = ((i // 3) * 3 + (j // 3))
        #             if val in rows[i] or val in cols[j] or val in squares[squares_index]:
        #                 return False
        #             rows[i].add(val)
        #             cols[j].add(val)
        #             squares[squares_index].add(val)
        
        # return True

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                squares_index = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in squares[squares_index]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[squares_index].add(val)
        
        return True
