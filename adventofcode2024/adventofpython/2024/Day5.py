from Day0 import Day0


def check(rules, update):
    correct = True
    for i in range(len(update) - 1):
        if '|'.join(update[l] for l in range(i, i + 2)) not in rules:
            correct = False
            break
    return correct


class Day5(Day0):

    def part_one(self):
        res = 0
        rules = [self.input[i] for i in range(self.input.index(''))]
        updates = [self.input[i].split(',') for i in range(self.input.index('') + 1, len(self.input))]
        for update in updates:
            if check(rules, update):
                res += int(update[int(len(update) / 2)])

        print(res)


    def part_two(self):
        res = 0
        rules = [self.input[i] for i in range(self.input.index(''))]
        updates = [self.input[i].split(',') for i in range(self.input.index('') + 1, len(self.input))]
        for update in updates:
            if not check(rules, update):
                while True:
                    for i in range(len(update) - 1):
                        slic = update[i] + '|' + update[i+1]
                        rev_slic = update[i+1] + '|' + update[i]
                        if slic not in rules and rev_slic in rules:
                            tmp = update[i]
                            update[i] = update[i + 1]
                            update[i + 1] = tmp
                    if check(rules, update):
                        break
                res += int(update[int(len(update) / 2)])

        print(res)


day='5'

print('Day5 Part1 Test')
Day5('2024', 'day' + day + '_test.txt').part_one()
print('Day5 Part1')
Day5('2024', 'day' + day + '.txt').part_one()
print('Day5 Part2 Test')
Day5('2024', 'day' + day + '_test.txt').part_two()
print('Day5 Part2')
Day5('2024', 'day' + day + '.txt').part_two()
