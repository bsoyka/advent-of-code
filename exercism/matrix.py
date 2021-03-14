class Matrix(object):
    def __init__(self, matrix_string: str):
        self.matrix = []
        for row in matrix_string.split("\n"):
            self.matrix.append([int(cell) for cell in row.split(" ")])

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
