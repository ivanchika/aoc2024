from Day0 import Day0
import collections

goal = 'E'
wall = '#'


def find_shortest_path(grid, start):
    shortest = None
    height = len(grid)
    width = len(grid[0])
    queue = collections.deque([[start]])
    seen = {start}
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if grid[y][x] == goal:
            res = len(path) - 1
            if not shortest:
                shortest = res
            else:
                shortest = min(shortest, res)
        for y2, x2 in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (y2, x2) not in seen:
                queue.append(path + [(y2, x2)])
                seen.add((y2, x2))
    return shortest


class Day20(Day0):

    def part_one(self):
        res = 0
        start = None
        for i in range(len(self.input)):
            if 'S' in self.input[i]:
                start = (i, self.input[i].index('S'))
                break
        no_cheat_shortest = find_shortest_path(self.input, start)
        print(no_cheat_shortest)
        # for r in range(len(self.input)):
        #     print(''.join('O' if (c, r) in path else self.input[r][c] for c in range(len(self.input[0]))))
        # print(res)

    def part_two(self):
        res = 0
        print(res)


day='20'

print('Day20 Part1 Test')
Day20('2024', 'day' + day + '_test.txt').part_one()
# print('Day20 Part1')
# Day20('2024', 'day' + day + '.txt').part_one()
# print('Day20 Part2 Test')
# Day20('2024', 'day' + day + '_test.txt').part_two()
# print('Day20 Part2')
# Day20('2024', 'day' + day + '.txt').part_two()
