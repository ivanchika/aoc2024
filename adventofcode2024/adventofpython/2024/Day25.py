import operator


from Day0 import Day0


class Day25(Day0):

    def part_one(self):
        res = 0
        keys = []
        locks = []
        data = self.input
        cols = len(data[0])
        rows = data.index('')
        max_digit = rows - 2
        for r in range(0, len(data), rows + 1):
                if data[r][0] == '#':
                    number = [0, 0, 0, 0, 0]
                    for i in range(r + 1, r + rows):
                        for j in range(cols):
                            number[j] += 1 if data[i][j] == '#' else 0
                    locks.append(tuple(number))
                else:
                    number = [0, 0, 0, 0, 0]
                    for i in range(r, r + rows - 1):
                        for j in range(cols):
                            number[j] += 1 if data[i][j] == '#' else 0
                    keys.append(tuple(number))

        for lock in locks:
            for key in keys:
                diff = list(filter(lambda d : d > max_digit, list(map(operator.add, lock, key))))
                print(lock, key, diff)
                if len(diff) == 0:
                    res += 1
        print(res)


    def part_two(self):
        res = 0
        print(res)


day='25'

# print('Day25 Part25 Test')
# Day25('2024', 'day' + day + '_test.txt').part_one()
print('Day25 Part25')
Day25('2024', 'day' + day + '.txt').part_one()
#print('Day25 Part2 Test')
#Day25('2024', 'day' + day + '_test.txt').part_two()
#print('Day25 Part2')
#Day25('2024', 'day' + day + '.txt').part_two()
