from Day0 import Day0
import re


def calculate(line):
    res = 0
    for gem in re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', line):
        res += int(gem[0]) * int(gem[1])
    return res


class Day3(Day0):

    def part_one(self):
        print(calculate(self.read_line()))

    def part_two(self):
        res = 0
        for item in re.split(r"do\(\)", self.read_line()):
            res += calculate(re.split(r"don't\(\)", item)[0])
        print(res)


day='3'

print('Day3 Part1 Test')
Day3('2024', 'day' + day + '_test.txt').part_one()
print('Day3 Part1')
Day3('2024', 'day' + day + '.txt').part_one()
print('Day3 Part2 Test')
Day3('2024', 'day' + day + '_test2.txt').part_two()
print('Day3 Part2')
Day3('2024', 'day' + day + '.txt').part_two()
