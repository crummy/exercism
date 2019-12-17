from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix: List[List[int]] = [[int(x) for x in i.split(" ")] for i in matrix_string.split("\n")]

    def row(self, index: int) -> List[int]:
        return self.matrix[index - 1]

    def column(self, index: int) -> List[int]:
        return [self.matrix[i][index - 1] for i in range(len(self.matrix))]
