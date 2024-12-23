from Day0 import Day0
from collections import defaultdict, deque, Counter

goal = 'E'
wall = '#'

def find_shortest_path(grid, start):
    height = len(grid)
    width = len(grid[0])
    queue = deque([([start], {start: 0})])
    paths = []
    while queue:
        path = queue.popleft()
        y, x = path[0][-1]
        visited = path[1]

        if grid[y][x] == goal:
            return path

        for step in ((-1, 0), (0, 1), (1, 0),(0, -1)):
                y2 = y + step[0]
                x2 = x + step[1]
                if 1 <= x2 < width - 1 and 1 <= y2 < height - 1:
                    if (y2, x2) not in visited.keys():
                        if grid[y2][x2] != wall:
                                visited_copy = visited.copy()
                                visited_copy[(y2, x2)] = len(path[0])
                                queue.append((path[0] + [(y2, x2)], visited_copy))
    return paths

def find_shortest_cheated_path(shorted, onion):
    cheats = defaultdict(int)
    idx_from = 0
    while idx_from < len(shorted) - onion:
        for idx_to in range(idx_from + onion, len(shorted)):
            from_path_step = shorted[idx_from]
            to_path_step = shorted[idx_to]
            cur_onion = abs(from_path_step[0] - to_path_step[0]) + abs(from_path_step[1] - to_path_step[1])
            if cur_onion > onion:
                continue
            cheats[idx_to - idx_from - cur_onion] += 1
        idx_from += 1
    return cheats

class Day20(Day0):

    def part_one(self):
        res = 0
        start = None
        for i in range(len(self.input)):
            if 'S' in self.input[i]:
                start = (i, self.input[i].index('S'))
                break

        no_cheat_shortest_path = find_shortest_path(self.input, start)
        cheated = find_shortest_cheated_path(no_cheat_shortest_path[0], 2)

        for picos, times in cheated.items():
            if picos >= 100:
                print(picos, times)
                res += times
        print(res)

    def part_two(self):
        res = 0
        start = None
        for i in range(len(self.input)):
            if 'S' in self.input[i]:
                start = (i, self.input[i].index('S'))
                break

        shorted_path = find_shortest_path(self.input, start)

        cheated = find_shortest_cheated_path(shorted_path[0], 20)

        for picos, times in cheated.items():
            if picos >= 100:
                print(picos, times)
                res += times

        print(res)


day='20'

# print('Day20 Part1 Test')
# Day20('2024', 'day' + day + '_test.txt').part_one()
# print('Day20 Part1')
# Day20('2024', 'day' + day + '.txt').part_one()
# print('Day20 Part2 Test')
# Day20('2024', 'day' + day + '_test.txt').part_two()
print('Day20 Part2')
Day20('2024', 'day' + day + '.txt').part_two()
