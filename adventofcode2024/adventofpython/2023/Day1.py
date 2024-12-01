import re
from Day0 import Day0


class Day1(Day0):

    def part_one(self):
        res = 0
        for line in self.read_lines():
            replaced = re.sub('[a-z]', "", line)
            res += int(replaced[0] + replaced[-1])
        print(res)

    def part_two(self):
        res = 0
        for line in self.read_lines():
            parsed = ''
            for i in range(0, len(line)):
                if line[i].isdigit():
                    parsed += line[i]
                else:
                    part = line[i:i+5]
                    if part.startswith('one'):
                        parsed += '1'
                    if part.startswith('two'):
                        parsed += '2'
                    if part.startswith('three'):
                        parsed += '3'
                    if part.startswith('four'):
                        parsed += '4'
                    if part.startswith('five'):
                        parsed += '5'
                    if part.startswith('six'):
                        parsed += '6'
                    if part.startswith('seven'):
                        parsed += '7'
                    if part.startswith('eight'):
                        parsed += '8'
                    if part.startswith('nine'):
                        parsed += '9'

            res += int(parsed[0] + parsed[-1])
        print(res)


print("Day1 test 1:")
Day1('2023', 'day1_test.txt').part_one()
print("Day2 test 2:")
Day1('2023', 'day1_test2.txt').part_two()
print("Day1 part 1:")
Day1('2023', 'day1.txt').part_one()
print("Day1 part 2:")
Day1('2023', 'day1.txt').part_two()
