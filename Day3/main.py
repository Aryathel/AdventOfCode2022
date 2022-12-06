from utils import AdventOfCode2022Day


class Day3(AdventOfCode2022Day, day=3):
    @staticmethod
    def get_char_val(char: str) -> int:
        """Get the scoring value for an individual character.

        a-z = 1...26
        A-Z = 27...52
        """
        if char.isupper():
            return ord(char) - ord('A') + 27
        else:
            return ord(char) - ord('a') + 1

    def step_1(self) -> int:
        score = 0
        for sack in self.input.split('\n'):
            # Split the sack in half, convert them to sets.
            comp1 = set(sack[:int(len(sack)/2)])
            comp2 = set(sack[int(len(sack)/2):])

            # Use the set "intersection" method to find the matching character
            char = comp1.intersection(comp2).pop()

            # Add the score for the character
            score += self.get_char_val(char)
        return score

    def step_2(self) -> int:
        score = 0
        sacks = self.input.split('\n')

        # Increment by indexes 0 to the number of sacks, by 3.
        for i in range(0, len(sacks), 3):
            # Make three sets out of each group of three sacks
            sack1 = set(sacks[i])
            sack2 = set(sacks[i+1])
            sack3 = set(sacks[i+2])

            # The processing is the same as step 1, but with one extra set.
            char = sack1.intersection(sack2).intersection(sack3).pop()
            score += self.get_char_val(char)
        return score

    def run(self) -> None:
        self.header()
        print(f'Step 1: {self.step_1()}')
        print(f'Step 2: {self.step_2()}')


if __name__ == "__main__":
    Day3().run()
