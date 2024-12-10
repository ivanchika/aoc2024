from Day0 import Day0

def print_line(pairs):
    print('line=', build_line(pairs))

def build_line(pairs):
    return ''.join('.' if pair[0] == -1 else str(pair[0]) for pair in pairs for _ in range(int(pair[1])))

def calculate(pairs):
    res = 0
    line = ''.join('.' if pair[0] == -1 else str(pair[0]) for pair in pairs for _ in range(int(pair[1])))
    for i in range(len(line)):
        res += 0 if line[i] == '.' else i * int(line[i])
    return res

class Day9(Day0):

    def part_one(self):
        res = 0
        items = list(map(int, list(self.input[0])))
        blocks = list('.' if i % 2 != 0 else str(int(i / 2)) for i in range(len(items)) for _ in range(items[i]))

        i = 0
        while i < len(blocks):
            if blocks[i] == '.':
                blocks[i] = blocks.pop()
                while len(blocks) > 0 and blocks[-1] == '.':
                    blocks.pop()
            i += 1
        for m in range(len(blocks)):
            res += m * int(blocks[m])

        print(res)


    def part_two(self):
        pass

day='9'

print('Day9 Part1 Test')
Day9('2024', 'day' + day + '_test.txt').part_one()
print('Day9 Part1')
Day9('2024', 'day' + day + '.txt').part_one()
# print('Day9 Part2 Test')
# Day9('2024', 'day' + day + '_test.txt').part_two()
# print('Day9 Part2')
# Day9('2024', 'day' + day + '.txt').part_two()
