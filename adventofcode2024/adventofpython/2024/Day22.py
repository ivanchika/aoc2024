from Day0 import Day0

class Day22(Day0):

    def part_one(self):
        sec_numbers = [int(n) for n in self.input]
        for i in range(len(sec_numbers)):
            sec_num = sec_numbers[i]
            for step in range(2000):
                sec_num = ((sec_num * 64) ^ sec_num) % 16777216
                sec_num = ((sec_num // 32) ^ sec_num) % 16777216
                sec_num = ((sec_num * 2048) ^ sec_num) % 16777216
            sec_numbers[i] = sec_num
        print(sum(sec_numbers))

    def part_two(self):
        sec_numbers = [int(n) for n in self.input]
        res = {}
        for sec_num in sec_numbers:
            reg = set()
            seq = list()
            prev = len(sec_numbers) * 9 + 1
            for step in range(2000):
                sec_num = ((sec_num * 64) ^ sec_num) % 16777216
                sec_num = ((sec_num // 32) ^ sec_num) % 16777216
                sec_num = ((sec_num * 2048) ^ sec_num) % 16777216
                cur = sec_num % 10
                diff = cur - prev
                seq.append(diff)
                if len(seq) > 4:
                    seq.pop(0)
                prev = cur
                if len(seq) == 4:
                    tup = tuple(seq)
                    if tup not in reg:
                        if tup not in res.keys():
                            res[tup] = cur
                        else:
                            res[tup] += cur
                    reg.add(tup)

        print(max(res.values()))
day='22'

# print('Day22 Part22 Test')
# Day22('2024', 'day' + day + '_test.txt').part_one()
# print('Day22 Part22')
# Day22('2024', 'day' + day + '.txt').part_one()
# print('Day22 Part2 Test')
# Day22('2024', 'day' + day + '_test.txt').part_two()
print('Day22 Part2')
Day22('2024', 'day' + day + '.txt').part_two()
