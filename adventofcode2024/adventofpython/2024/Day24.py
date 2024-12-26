from Day0 import Day0
from collections import defaultdict

operators = {
    'OR': lambda a, b: a | b,
    'AND': lambda a, b: a & b,
    'XOR': lambda a, b: a ^ b
}

class Day24(Day0):

    def part_one(self):
        res = ''
        results = defaultdict()
        formulas = defaultdict()
        data = self.input
        for i in range(data.index('')):
            item = data[i].split(': ')
            results[item[0]] = int(item[1])
        for i in range(data.index('') + 1, len(data)):
            l = data[i].split(' -> ')
            a, op, b = l[0].split(' ')
            val = l[1]
            formulas[val] = (a, op, b)

        def calc(zk, fs):
            if zk in results.keys():
                return results[zk]
            else:
                aa, opp, bb = fs[zk]
                results[zk] = operators[opp](calc(aa, fs), calc(bb, fs))
                return results[zk]

        for z in reversed(sorted(filter(lambda k : k[0] == 'z', formulas.keys()))):
            res += str(calc(z, formulas))
        print(res)
        print(int(res, 2))


    def part_two(self):
        res = 0
        print(res)


day='24'

# print('Day24 Part24 Test')
# Day24('2024', 'day' + day + '_test.txt').part_one()
print('Day24 Part24')
Day24('2024', 'day' + day + '.txt').part_one()
#print('Day24 Part2 Test')
#Day24('2024', 'day' + day + '_test.txt').part_two()
#print('Day24 Part2')
#Day24('2024', 'day' + day + '.txt').part_two()
