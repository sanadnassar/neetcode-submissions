class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        number_rows = len(matrix)
        for rows in range(number_rows):
            for cols in range(0, rows+1):
                temp = matrix[rows][cols]
                matrix[rows][cols] = matrix[cols][rows]
                matrix[cols][rows] = temp
        for rows in matrix:
            rows.reverse()
