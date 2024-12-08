from itertools import product, combinations

from Day0 import Day0

def print_field(field, antinodes):
    list(map(lambda i : print(''.join(list('#' if field[i][j] == '.' and (i, j) in antinodes else field[i][j] for j in range(len(field[i]))))), range(len(field))))

def parse_antennas(field):
    return dict((ant:=field[y][x], list((y,x) for y in range(len(field)) for x in range(len(field)) if field[y][x] == ant))
                for y in range(len(field)) for x in range(len(field)) if field[y][x] != '.')

def calculate(field, second_part=False):
    rn = len(field)
    cn = len(field[0])
    antennas = parse_antennas(field)
    antinodes = set()

    for antenna in antennas.keys():
        items = antennas[antenna]
        combos = list(combinations(items, 2))
        for comb in combos:
            a = comb[0]
            b = comb[1]
            ydiff = a[0] - b[0]
            xdiff = a[1] - b[1]
            ny = a[0] + ydiff
            nx = a[1] + xdiff
            while 0 <= ny < rn and 0 <= nx < cn:
                antinodes.add((ny, nx))
                if second_part:
                    ny += ydiff
                    nx += xdiff
                else:
                    break
            ny = b[0] - ydiff
            nx = b[1] - xdiff
            while 0 <= ny < rn and 0 <= nx < cn:
                antinodes.add((ny, nx))
                if second_part:
                    ny -= ydiff
                    nx -= xdiff
                else:
                    break
            if second_part:
                antinodes.add(a)
                antinodes.add(b)

    print_field(field, antinodes)
    print('\nantinodes:{0}\n'.format(len(antinodes)))

class Day8(Day0):

    def part_one(self):
        calculate(self.input)

    def part_two(self):
        calculate(self.input, True)

day='8'

print('Day8 Part1 Test')
Day8('2024', 'day' + day + '_test.txt').part_one()
print('Day8 Part1')
Day8('2024', 'day' + day + '.txt').part_one()
print('Day8 Part2 Test')
Day8('2024', 'day' + day + '_test.txt').part_two()
print('Day8 Part2')
Day8('2024', 'day' + day + '.txt').part_two()
