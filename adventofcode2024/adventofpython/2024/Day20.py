from Day0 import Day0
import collections

goal = 'E'
wall = '#'
cheats = []

def find_shortest_path(grid, start, cheat_possible = False, shorted_visited = None):
    global cheats
    height = len(grid)
    width = len(grid[0])
    queue = collections.deque([([start], None, {start: 0})])
    paths = []
    while queue:
        path = queue.popleft()
        y, x = path[0][-1]
        cheat = path[1]
        visited = path[2]
        if cheat and visited[(y, x)] < shorted_visited[y, x]:
            paths.append((shorted_visited[y, x] - visited[(y, x)], cheat))
            continue
        elif grid[y][x] == goal and not cheat_possible:
            return path

        for step in ((-1, 0), (0, 1), (1, 0),(0, -1)):
                y2 = y + step[0]
                x2 = x + step[1]
                if 1 <= x2 < width - 1 and 1 <= y2 < height - 1:
                    if (y2, x2) not in visited.keys():
                        if grid[y2][x2] != wall:
                                visited_copy = visited.copy()
                                visited_copy[(y2, x2)] = len(path[0]) + 1
                                queue.append((path[0] + [(y2, x2)], cheat, visited_copy))
                        elif cheat_possible and not cheat and (y2, x2, step) not in cheats:
                            sim_y = y2 + step[0]
                            sim_x = x2 + step[1]
                            if 1 <= sim_y < width - 1 and 1 <= sim_x < height - 1 and grid[sim_y][sim_x] != wall  and (sim_y, sim_x) not in visited.keys():
                                visited_copy = visited.copy()
                                visited_copy[(y2, x2)] = len(path[0]) + 1
                                visited_copy[(sim_y, sim_x)] = len(path[0]) + 2
                                cheated_path = path[0] + [(y2, x2)] + [(sim_y, sim_x)]
                                cheats.append((y2, x2, step))
                                queue.append((cheated_path, (y2, x2, step), visited_copy))
    return paths


class Day20(Day0):

    def part_one(self):
        global cheats
        start = None
        for i in range(len(self.input)):
            if 'S' in self.input[i]:
                start = (i, self.input[i].index('S'))
                break
        no_cheat_shortest_path = find_shortest_path(self.input, start)
        shortest_visited = no_cheat_shortest_path[2]
        cheated_shortest = find_shortest_path(self.input, start, True, shortest_visited)
        counter = collections.Counter([d[0] for d in cheated_shortest])
        print(counter)
        print(sum(1 for che in cheated_shortest if che[0] >= 100))

    def part_two(self):
        res = 0
        print(res)


day='20'

print('Day20 Part1 Test')
Day20('2024', 'day' + day + '_test.txt').part_one()
print('Day20 Part1')
Day20('2024', 'day' + day + '.txt').part_one()
# print('Day20 Part2 Test')
# Day20('2024', 'day' + day + '_test.txt').part_two()
# print('Day20 Part2')
# Day20('2024', 'day' + day + '.txt').part_two()
