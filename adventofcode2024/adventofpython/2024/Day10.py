from Day0 import Day0

def find_trail(array, i, j, lookup, path, trailheads, paths):
    if i < 0 or i == len(array) or j < 0 or j == len(array[i]) or array[i][j] == '.':
        return
    curr = int(array[i][j])

    path += '||{0}:{1}'.format(i, j)
    if curr == lookup and curr == 9:
        trailheads.add((i,j))
        paths.add(path)
    elif curr == lookup or lookup == 0:
        find_trail(array, i - 1, j, lookup + 1, path, trailheads, paths)
        find_trail(array, i, j - 1, lookup + 1, path, trailheads, paths)
        find_trail(array, i + 1, j, lookup + 1, path, trailheads, paths)
        find_trail(array, i, j + 1, lookup + 1, path, trailheads, paths)

def calculate(array):
    part_one = 0
    part_two = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == '0':
                trailheads = set([])
                paths = set([])
                find_trail(array, i, j, 0, '', trailheads, paths)
                part_one += len(trailheads)
                part_two += len(paths)
    return part_one, part_two

class Day10(Day0):

    def __init__(self, year, input_filename):
        super().__init__(year, input_filename)
        self.res = calculate(self.input)

    def part_one(self):
        print(self.res[0])


    def part_two(self):
        print(self.res[1])


day='10'

print('Day10 Part1 Test')
Day10('2024', 'day' + day + '_test.txt').part_one()
print('Day10 Part1')
Day10('2024', 'day' + day + '.txt').part_one()
print('Day10 Part2 Test')
Day10('2024', 'day' + day + '_test.txt').part_two()
print('Day10 Part2')
Day10('2024', 'day' + day + '.txt').part_two()
