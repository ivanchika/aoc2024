from Day0 import Day0
import collections

goal = 'E'
wall = '#'


def find_shortest_path(grid, start):
    height = len(grid)
    width = len(grid[0])
    queue = collections.deque([[start]])
    seen = {start}
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if grid[y][x] == goal:
            return path
        for y2, x2 in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (y2, x2) not in seen:
                queue.append(path + [(y2, x2)])
                seen.add((y2, x2))


class Day16(Day0):

    def part_one(self):
        res = 0
        start = None
        direction = (1, 0)
        for i in range(len(self.input)):
            if 'S' in self.input[i]:
                start = (i, self.input[i].index('S'))
                break
        print(start)
        path = find_shortest_path(self.input, start)
        print(path)
        for r in range(len(self.input)):
            print(''.join('O' if (c, r) in path else self.input[r][c] for c in range(len(self.input[0]))))
        for s in range(len(path) - 1):
            current = (path[s + 1][0] - path[s][0], path[s + 1][1] - path[s][1])
            if current != direction:
                res += 1000
                direction = current
            else:
                res += 1
        print(res)


    def part_two(self):
        res = 0
        print(res)


day='16'

print('Day16 Part1 Test')
Day16('2024', 'day' + day + '_test.txt').part_one()
# print('Day16 Part1')
# Day16('2024', 'day' + day + '.txt').part_one()
# print('Day16 Part2 Test')
# Day16('2024', 'day' + day + '_test.txt').part_two()
# print('Day16 Part2')
# Day16('2024', 'day' + day + '.txt').part_two()
