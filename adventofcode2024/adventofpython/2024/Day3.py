from Day0 import Day0
import re

class Day3(Day0):

    def part_one(self):
        res = 0
        line = self.read_line()
        found = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
        for gem in found:
            replaced = gem.replace("mul(", "").replace(")", "").split(",")
            res += int(replaced[0]) * int (replaced[1])
        print(res)


    def part_two(self):
        res = 0
        line = self.read_line()
        filtered = re.split(r"don't\(\).+do\(\)", line)
        print(filtered)
        print(len(filtered))
        for item in filtered:
            found = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', item)
            for gem in found:
                numbers = re.findall(r'[0-9]{1,3}', gem)
                res += int(numbers[0]) * int (numbers[1])
        print(res)


day='3'

# print('Day3 Part1 Test')
# Day3('2024', 'day' + day + '_test.txt').part_one()
# print('Day3 Part1')
# Day3('2024', 'day' + day + '.txt').part_one()
print('Day3 Part2 Test')
Day3('2024', 'day' + day + '_test2.txt').part_two()
print('Day3 Part2')
Day3('2024', 'day' + day + '.txt').part_two()
