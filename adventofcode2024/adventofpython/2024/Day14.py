from Day0 import Day0
import re

class Day14(Day0):

    def part_one(self):
        robots = [[int(a), int(b), int(c), int(d)] for line in self.input for a, b, c, d in re.findall(r'p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)', line)]

        rows = 103
        cols = 101
        seconds = 100
        for i in range(len(robots)):
            robots[i][0] = (robots[i][0] + (robots[i][2] * seconds)) % cols
            robots[i][1] = (robots[i][1] + (robots[i][3] * seconds)) % rows
        lu, ru, ld, rd = 0, 0, 0, 0
        mid_x = int(cols / 2)
        mid_y = int(rows / 2)
        for robot in robots:
            if robot[0] < mid_x and robot[1] < mid_y:
                lu += 1
            elif robot[0] > mid_x and robot[1] < mid_y:
                ru += 1
            elif robot[0] < mid_x and robot[1] > mid_y:
                ld +=1
            elif robot[0] > mid_x and robot[1] > mid_y:
                rd += 1
        res = lu * ru * ld * rd
        print(res)


    def part_two(self):
        robots = [[int(a), int(b), int(c), int(d)] for line in self.input for a, b, c, d in re.findall(r'p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)', line)]

        seconds = 0
        while True:
            seconds += 1
            for i in range(len(robots)):
                robots[i][0] = (robots[i][0] + robots[i][2]) % 101
                robots[i][1] = (robots[i][1] + robots[i][3]) % 103
            if len(list(filter(lambda robot : 50 - robot[1] <= robot[0] <= 50 + robot[1], robots))) > 450:
                break
        print(seconds)

day='14'

# print('Day14 Part1 Test')
# Day14('2024', 'day' + day + '_test.txt').part_one()
print('Day14 Part1')
Day14('2024', 'day' + day + '.txt').part_one()
# print('Day14 Part2 Test')
# Day14('2024', 'day' + day + '_test.txt').part_two()
print('Day14 Part2')
Day14('2024', 'day' + day + '.txt').part_two()
