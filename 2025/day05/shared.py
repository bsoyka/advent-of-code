class FreshRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @classmethod
    def from_input_line(cls, line: str):
        start, end = map(int, line.split("-"))
        return cls(start, end)

    def contains(self, value):
        return self.start <= value <= self.end

    @property
    def size(self):
        return self.end - self.start + 1
