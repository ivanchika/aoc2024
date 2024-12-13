from Day0 import Day0
import re

but_a_regexp = r'Button A\: X\+([0-9]+), Y\+([0-9]+)'
but_b_regexp = r'Button B\: X\+([0-9]+), Y\+([0-9]+)'
prize_regexp = r'Prize\: X=([0-9]+), Y=([0-9]+)'

def parse_input(data, plus = 0):
    parsed = []
    for line in zip(*[iter(data)] * 3):
        but_a_s = re.findall(but_a_regexp, line[0])[0]
        but_b_s = re.findall(but_b_regexp, line[1])[0]
        prize_s = re.findall(prize_regexp, line[2])[0]
        but_a = (int(but_a_s[0]), int(but_a_s[1]))
        but_b = (int(but_b_s[0]), int(but_b_s[1]))
        prize = (int(prize_s[0]) + plus, int(prize_s[1]) + plus)
        parsed.append((but_a, but_b, prize))
    return parsed

class Day13(Day0):

    def part_one(self):
        res = 0
        for but_a, but_b, prize in parse_input(list(filter(lambda l : l!= '', self.input))):
            pressed_a = 0
            while True:
                pressed_a += 1
                if pressed_a > 100:
                    break
                left_x = prize[0] - (but_a[0] * pressed_a)
                left_y = prize[1] - (but_a[1] * pressed_a)
                if left_x >= 0 and left_y >= 0 and left_x % but_b[0] == 0 and left_y % but_b[1] == 0:
                    pressed_b = int(left_x / but_b[0])
                    if pressed_b <= 100 and left_y == pressed_b * but_b[1]:
                        score = pressed_a * 3 + pressed_b
                        res += score
                        break
        print(res)


    def part_two(self):
        res = 0
        for but_a, but_b, prize in parse_input(list(filter(lambda l : l!= '', self.input)), 10000000000000):
            line_a = but_a[1] / but_a[0]
            line_b = but_b[1] / but_b[0]
            xs = (-(prize[1] - line_a * prize[0])) / (line_a - line_b)
            p_b = xs / but_b[0]
            p_a = (prize[0] - xs) / but_a[0]
            p_a_r = round(p_a)
            p_b_r = round(p_b)
            if abs(p_a_r - p_a) < 0.01 and abs(p_b_r - p_b) < 0.01:
                res += p_a_r * 3 + p_b_r
        print(res)


day='13'

print('Day13 Part1 Test')
Day13('2024', 'day' + day + '_test.txt').part_one()
print('Day13 Part1')
Day13('2024', 'day' + day + '.txt').part_one()
print('Day13 Part2 Test')
Day13('2024', 'day' + day + '_test.txt').part_two()
print('Day13 Part2')
Day13('2024', 'day' + day + '.txt').part_two()
