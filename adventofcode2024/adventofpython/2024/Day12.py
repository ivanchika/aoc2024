from Day0 import Day0

def find_region(garden, i, j):
    plant = garden[i][j]
    region = set()
    queue = {(i, j)}
    while queue:
        i, j = queue.pop()
        region.add((i, j))
        for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
            if (x in range(len(garden[0])) and
                    y in range(len(garden)) and
                    garden[x][y] == plant and
                    (x, y) not in region and
                    (x, y) not in queue
            ):
                queue.add((x, y))

    corners = sum(count_corners(garden, x, y) for x, y in region)
    return region, corners * len(region)

def count_corners(garden, i, j):
    UL, L, DL, U, D, UR, R, DR = [
        i+x in range(len(garden)) and j+y in range(len(garden[0])) and garden[i+x][j+y] == garden[i][j]
        for x in range(-1, 2)
        for y in range(-1, 2)
        if x or y
    ]
    return sum([
        U and L and not UL,
        U and R and not UR,
        D and L and not DL,
        D and R and not DR,
        not (U or L),
        not (U or R),
        not (D or L),
        not (D or R)
    ])

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
        visited = set()
        garden = self.input
        for i in range(len(garden)):
            for j in range(len(garden[0])):
                if (i, j) not in visited:
                    visited_region, cost = find_region(garden, i, j)
                    res += cost
                    visited |= visited_region
        print(res)

day='12'

# print('Day12 Part1 Test')
# Day12('2024', 'day' + day + '_test.txt').part_one()
# print('Day12 Part1')
# Day12('2024', 'day' + day + '.txt').part_one()
print('Day12 Part2 Test')
Day12('2024', 'day' + day + '_test.txt').part_two()
print('Day12 Part2')
Day12('2024', 'day' + day + '.txt').part_two()
