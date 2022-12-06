from utils import AdventOfCode2022Day


class Day4(AdventOfCode2022Day, day=4):
    @staticmethod
    def process_assignment(inp: str) -> tuple[int, ...]:
        """Convert an assignment to an int tuple.

        2-6 -> (2, 6)
        """
        return tuple(int(i) for i in inp.split('-'))

    @staticmethod
    def process_pair(inp: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
        """Convert a pair of assignments to a tuple of tuples.

        2-6,3-4 -> ((2, 6), (3, 4))
        """
        pair1, pair2 = inp.split(',')
        return Day4.process_assignment(pair1), Day4.process_assignment(pair2)

    def step_1(self) -> int:
        count = 0
        for pair in self.input.split('\n'):
            # Process the row into usable values
            elf1, elf2 = self.process_pair(pair)

            # Check if the first assignment contains the second
            if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
                count += 1
            # Check if the second assignment contains the first
            elif elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
                count += 1

        return count

    def step_2(self) -> int:
        count = 0
        for pair in self.input.split('\n'):
            # Process the row into usable values.
            elf1, elf2 = self.process_pair(pair)

            # Check if the first assignment overlaps the second.
            if elf1[0] <= elf2[0] <= elf1[1]:
                count += 1
            # Check if the second assignment overlaps the first.
            elif elf2[0] <= elf1[0] <= elf2[1]:
                count += 1

        return count

    def run(self) -> None:
        self.header()
        print(f'Step 1: {self.step_1()}')
        print(f'Step 2: {self.step_2()}')


if __name__ == "__main__":
    Day4().run()
