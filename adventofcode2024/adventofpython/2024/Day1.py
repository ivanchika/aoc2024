from Day0 import Day0


class Day1(Day0):

    def part_one(self):
        res = 0
        lines = self.read_lines()
        left = []
        right = []
        for line in lines:
            parts = line.split('  ')
            left.append(int(parts[0]))
            right.append(int(parts[1]))
        left.sort()
        right.sort()
        for index in range(len(left)):
            res += abs(left[index] - right[index])

        print(res)


    def part_two(self):
        res = 0
        lines = self.read_lines()
        left = []
        right = []
        for line in lines:
            parts = line.split('  ')
            left.append(int(parts[0]))
            right.append(int(parts[1]))
        for index in range(len(left)):
            res += left[index] * right.count(left[index])

        print(res)
    

print('Day1 Part1 Test')
Day1('2024', 'day1_test.txt').part_one()
print('Day1 Part1')
Day1('2024', 'day1.txt').part_one()
print('Day1 Part2 Test')
Day1('2024', 'day1_test.txt').part_two()
print('Day1 Part2')
Day1('2024', 'day1.txt').part_two()