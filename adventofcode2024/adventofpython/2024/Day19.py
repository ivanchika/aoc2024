from Day0 import Day0


class Day19(Day0):

    def part_one(self):
        res = 0
        stripes = list(reversed(sorted(self.input[0].split(', '),key=len)))
        designs = self.input[2:]

        def check_sum_optimized(strips, des):
            sums1, sums2 = [], []
            stripes1 = strips[:len(strips) // 2]
            stripes2 = strips[len(strips) // 2:]

            for sums, stripes_ in ((sums1, stripes1), (sums2, stripes2)):
                for stripe in stripes_:
                    for sum_ in sums[:]:
                        sums.append(sum_ + stripe)

                    sums.append(stripe)

            for sum_ in sums1:
                if des.replace(sum_, '') in sums2:
                    return True

        all_d = len(designs)
        i = 1
        for design in designs:
            f_stripes = [stripe for stripe in stripes if design.count(stripe)]
            checked = check_sum_optimized(f_stripes, design)
            if checked:
                res += 1
            print(i, 'from', all_d, 'checked', design, checked)
        print(res)


    def part_two(self):
        res = 0
        print(res)


day='19'

print('Day19 Part19 Test')
Day19('2024', 'day' + day + '_test.txt').part_one()
# print('Day19 Part19')
# Day19('2024', 'day' + day + '.txt').part_one()
# print('Day19 Part2 Test')
# Day19('2024', 'day' + day + '_test.txt').part_two()
# print('Day19 Part2')
# Day19('2024', 'day' + day + '.txt').part_two()
