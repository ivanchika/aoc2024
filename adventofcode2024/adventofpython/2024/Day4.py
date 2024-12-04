from Day0 import Day0

xmas = 'XMAS'
mas = ['MAS', 'SAM']

def find_xmas(array, i, j, dir_i, dir_j):
    return (0 <= i + 3 * dir_i < len(array) and 0 <= j + 3 * dir_j < len(array[0])
            and xmas == ''.join(array[i + l * dir_i][j + l * dir_j] for l in range(4)))

def find_mas(array, i, j):
    return (''.join(array[i + a][j + a] for a in range(3)) in mas
            and ''.join(array[i  + 2 - a][j + a] for a in range(3)) in mas)


class Day4(Day0):

    def part_one(self):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]
        res = 0
        for i in range(len(self.input)):
            for j in range(len(self.input[0])):
                if self.input[i][j] == 'X':
                    for di, dj in directions:
                        if find_xmas(self.input, i, j, di, dj):
                            res += 1
        print(res)

    def part_two(self):
        res = 0
        for i in range(len(self.input) - 2):
            for j in range(len(self.input[0]) - 2):
                if find_mas(self.input, i, j):
                    res += 1
        print(res)

day='4'

print('Day4 Part1 Test')
Day4('2024', 'day' + day + '_test.txt').part_one()
print('Day4 Part1')
Day4('2024', 'day' + day + '.txt').part_one()
print('Day4 Part2 Test')
Day4('2024', 'day' + day + '_test2.txt').part_two()
print('Day4 Part2')
Day4('2024', 'day' + day + '.txt').part_two()
