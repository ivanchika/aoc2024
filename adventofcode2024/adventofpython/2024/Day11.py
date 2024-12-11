from Day0 import Day0

def blink(stone, blinks, cache):
    if (stone, blinks) in cache.keys():
        return cache[(stone, blinks)]
    if blinks == 0:
        return 1
    res = 0
    if stone == '0':
        res += blink('1', blinks - 1, cache)
    elif len(stone) % 2 == 0:
        stone_dig_len = int(len(stone) / 2)
        res += blink(str(int(stone[:stone_dig_len])), blinks - 1, cache)
        res += blink(str(int(stone[stone_dig_len:])), blinks - 1, cache)
    else:
        res += blink(str(int(stone) * 2024), blinks - 1, cache)
    cache[(stone, blinks)] = res
    return res

def calculate(data, blinks = 25):
    cache = {}
    return sum(blink(stone, blinks, cache) for stone in data[0].split(' '))

class Day11(Day0):

    def part_one(self):
        print(calculate(self.input))

    def part_two(self):
        print(calculate(self.input, 75))


day='11'

print('Day11 Part1 Test')
Day11('2024', 'day' + day + '_test.txt').part_one()
print('Day11 Part1')
Day11('2024', 'day' + day + '.txt').part_one()
print('Day11 Part2 Test')
Day11('2024', 'day' + day + '_test.txt').part_two()
print('Day11 Part2')
Day11('2024', 'day' + day + '.txt').part_two()
