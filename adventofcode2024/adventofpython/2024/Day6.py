from Day0 import Day0


def build_path(position, direction, array, obstruction=None):
    path, lines = set(), set()

    while True:
        if (line:=(position, direction)) in lines:
            return None
        lines.add(line)
        path.add(position)
        if not fetch(position + direction, array):
            return path
        elif fetch(next_position:= position + direction, array) == '#' or next_position == obstruction:
            direction *= -1j
        else:
            position = next_position

def fetch(position, array):
    r, c = int(position.real), int(position.imag)
    return None if not (0 <= r < len(array) and 0 <= c < len(array[0])) else array[r][c]

class Day6(Day0):

    def __init__(self, year, input_filename):
        super().__init__(year, input_filename)
        self.start_position = next(row + col * 1j for row in range(len(self.input)) for col in range(len(self.input[0])) if self.input[row][col] == '^')
        self.start_direction = -1 + 0j

    def part_one(self):
        print(len(build_path(self.start_position, self.start_direction, self.input)))

    def part_two(self):
        path = build_path(self.start_position, self.start_direction, self.input)
        print(sum(not build_path(self.start_position, self.start_direction, self.input, obstruction) for obstruction in path if fetch(obstruction, self.input) == '.'))

day='6'

print('Day6 Part1 Test')
Day6('2024', 'day' + day + '_test.txt').part_one()
print('Day6 Part1')
Day6('2024', 'day' + day + '.txt').part_one()
print('Day6 Part2 Test')
Day6('2024', 'day' + day + '_test.txt').part_two()
print('Day6 Part2')
Day6('2024', 'day' + day + '.txt').part_two()
