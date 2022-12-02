from utils import AdventOfCode2022Day


class Day1(AdventOfCode2022Day, day=1):
    def step_1(self) -> int:
        """Split the data into groups, then process each group's total and choose the highest one."""
        max_cal = -1
        for group in self.input.split('\n\n'):
            val = sum(int(cal) for cal in group.split('\n'))
            if val > max_cal:
                max_cal = val
        return max_cal

    def step_2(self) -> int:
        """Split the data into groups, the process each group's total and replace
        the lowest value in the top three if the current value is greater than it.
        """
        max_cals = [-1, -1, -1]
        for group in self.input.split('\n\n'):
            val = sum(int(cal) for cal in group.split('\n'))
            if any(val > cal for cal in max_cals):
                max_cals[max_cals.index(min(max_cals))] = val
        return sum(max_cals)

    def run(self) -> None:
        self.header()
        print(f'Step 1: {self.step_1()}')
        print(f'Step 2: {self.step_2()}')


if __name__ == "__main__":
    Day1().run()
