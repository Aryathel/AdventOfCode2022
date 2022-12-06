from utils import AdventOfCode2022Day


class Day6(AdventOfCode2022Day, day=6):
    def step_1(self) -> int:
        buff = self.input.strip()

        # Iterate o
        for i in range(4, len(buff)):
            if len(set(buff[i-4:i])) == 4:
                return i

    def step_2(self) -> int:
        buff = self.input.strip()

        for i in range(14, len(buff)):
            if len(set(buff[i-14:i])) == 14:
                return i

    def run(self) -> None:
        self.header()
        print(f'Step 1: {self.step_1()}')
        print(f'Step 2: {self.step_2()}')


if __name__ == "__main__":
    Day6().run()
