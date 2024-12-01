from abc import abstractmethod
from pathlib import Path


class Day0:

    def __init__(self, year, input_filename):
        self.path = Path("..", "resources", year, input_filename)

    @abstractmethod
    def part_one(self):
        pass

    @abstractmethod
    def part_two(self):
        pass

    def read_lines(self):
        return self.path.read_text().splitlines()

    def read_line(self):
        return self.path.read_text().splitlines()[0]
