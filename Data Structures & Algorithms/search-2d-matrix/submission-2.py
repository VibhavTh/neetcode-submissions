class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search(row, target):
            l = 0
            r = len(row) - 1

            while l <= r:
                m = (l + r) // 2

                if row[m] < target:
                    l = m + 1
                
                elif row[m] > target:
                    r = m - 1
                
                else:
                    return row[m]
            
            return -1
        
        for row in matrix:
            x = search(row, target)
            print(x)
            if search(row, target) != -1:
                return True
        
        return False