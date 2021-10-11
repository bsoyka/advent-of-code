from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = []

        for row in matrix_string.splitlines():
            self.matrix.append([int(cell) for cell in row.split(' ')])

    def row(self, index: int) -> List[int]:
        return self.matrix[index - 1]

    def column(self, index: int) -> List[int]:
        return [row[index - 1] for row in self.matrix]
