from Day0 import Day0


class Day2(Day0):

    def part_one(self):
        res = 0
        for line in self.read_lines():
            if is_line_safe(line.split(' ')):
                res += 1
        print(res)


    def part_two(self):
        res = 0
        for line in self.read_lines():
            items = line.split(' ')
            if is_line_safe(items):
                res += 1
            else:
                safe = False
                for item in range(len(items)):
                    all_items = line.split(' ')
                    del all_items[item]
                    if is_line_safe(all_items):
                        safe = True
                        break
                if safe is True:
                    res += 1
        print(res)

def is_line_safe(line):
    prev = None
    direction = None
    is_safe = True
    for item in line:
        if prev is None:
            prev = int(item)
        else:
            curr = int(item)
            if curr == prev or abs(curr - prev) > 3:
                is_safe = False
                break
            if direction is None:
                if curr > prev:
                    direction = 'i'
                else:
                    direction = 'd'
            elif direction == 'i':
                if curr < prev:
                    is_safe = False
                    break
            else:
                if curr > prev:
                    is_safe = False
                    break
            prev = curr

    return is_safe

day='2'

print('Day2 Part1 Test')
Day2('2024', 'day' + day + '_test.txt').part_one()
print('Day2 Part1')
Day2('2024', 'day' + day + '.txt').part_one()
print('Day2 Part2 Test')
Day2('2024', 'day' + day + '_test.txt').part_two()
print('Day2 Part2')
Day2('2024', 'day' + day + '.txt').part_two()
