from Day0 import Day0

class Day12(Day0):

    def part_one(self):
        garden = self.input
        res = 0
        visited = set()
        for i in range(len(garden)):
            for j in range(len(garden[0])):
                if (i, j) not in visited:
                    fence = 0
                    steps = [(i, j)]
                    visited_plants = set()
                    while steps:
                        r, c = steps.pop()
                        if (r, c) not in visited_plants:
                            if r not in range(len(garden)) or c not in range(len(garden[0])) or garden[r][c] != garden[i][j]:
                                fence += 1
                                continue
                            visited_plants.add((r, c))
                            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                if (r+x, c+y) not in visited_plants:
                                    steps.append((r+x, c+y))
                    res += len(visited_plants) * fence
                    visited |= visited_plants
        print(res)


    def part_two(self):
        res = 0
        print(res)

day='12'

print('Day12 Part1 Test')
Day12('2024', 'day' + day + '_test.txt').part_one()
print('Day12 Part1')
Day12('2024', 'day' + day + '.txt').part_one()
# print('Day12 Part2 Test')
# Day12('2024', 'day' + day + '_test.txt').part_two()
# print('Day12 Part2')
# Day12('2024', 'day' + day + '.txt').part_two()
