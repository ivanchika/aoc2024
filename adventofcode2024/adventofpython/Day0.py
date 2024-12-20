from abc import abstractmethod
from pathlib import Path


def print_array(array):
    for i in range(len(array)):
        line = ''.join(list(array[i][j] for j in range(array[i])))
        print(line)


class Day0:

    input = None

    def __init__(self, year, input_filename):
        self.path = Path("..", "resources", year, input_filename)
        self.input = self.read_lines()

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
