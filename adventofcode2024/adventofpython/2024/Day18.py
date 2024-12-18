from Day0 import Day0
import collections

m = 71
n = 71
goal = (m - 1, n - 1)
size = 1024

def find_shortest_path(walls, start):
    queue = collections.deque([[start]])
    seen = {start}
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if (y, x) == goal:
            return path
        for y2, x2 in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
            if 0 <= x2 < m and 0 <= y2 < n and (y2, x2) not in walls and (y2, x2) not in seen:
                queue.append(path + [(y2, x2)])
                seen.add((y2, x2))

class Day18(Day0):

    def part_one(self):
        walls = [(int(self.input[i].split(',')[0]), int(self.input[i].split(',')[1])) for i in range(size)]
        # for r in range(n):
        #     print(''.join('#' if (c, r) in walls else '.' for c in range(m)))
        print(len(find_shortest_path(walls, (0,0))) - 1)

    def part_two(self):
        walls = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in self.input]
        walls_num = len(walls) - 1
        while True:
            if find_shortest_path(walls[:walls_num], (0,0)) is not None:
                print('{0},{1}'.format(walls[walls_num][0], walls[walls_num][1]))
                break
            walls_num -= 1

day='18'

# print('Day18 Part18 Test')
# Day18('2024', 'day' + day + '_test.txt').part_one()
print('Day18 Part18')
Day18('2024', 'day' + day + '.txt').part_one()
# print('Day18 Part2 Test')
# Day18('2024', 'day' + day + '_test.txt').part_two()
print('Day18 Part2')
Day18('2024', 'day' + day + '.txt').part_two()
