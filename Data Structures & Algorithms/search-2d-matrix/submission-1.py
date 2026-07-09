class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = (len(matrix) * len(matrix[0]))-1

        while (left <= right):
            mid = math.ceil((left+right) / 2)
            
            row = mid // (len(matrix[0]))
            col = mid % (len(matrix[0]))
            print(f"Row:{row}, Col:{col}")

            if (matrix[row][col] == target):
                return True
            if (matrix[row][col] < target):
                left=mid+1
            if (matrix[row][col] > target):
                right=mid-1
            
        return False


        
        