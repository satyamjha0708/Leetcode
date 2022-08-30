class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
                for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        if i<j:
                            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]


                for i in matrix:
                    i.reverse()


                return matrix