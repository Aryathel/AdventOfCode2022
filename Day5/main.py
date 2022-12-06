from utils import AdventOfCode2022Day


class Day5(AdventOfCode2022Day, day=5):
    @staticmethod
    def process_stack(layout: str) -> dict[int, list[str]]:
        """Convert a text drawing input or stacked boxes to a usable
        data structure.

        [A]
        [B] [D]
        [C] [E] [F]
         1   2   3

        {1: ['C'], 'B', 'A'], 2: ['E', 'D'], 3: ['F']}
        """
        rows = layout.split('\n')

        # Create the columns from the bottom row of numbers.
        stacks = {int(i): list() for i in rows[-1].strip().split('   ')}

        # Process the box stacks from the bottom up.
        # This leaves the boxes on top of each stack at the end of the lists.
        for row in reversed(rows[:-1]):
            for col in stacks:
                # Use som tricky string indexing to get the character for a box.
                # The box characters can be found at indexes 1, 5, 9, 13, etc.
                char = row[1 + ((col-1) * 4)]

                # Ensure that the character is not a blank space.
                if char.isalpha():
                    # Add the character to the stack list
                    stacks[col].append(char)

        return stacks

    @staticmethod
    def process_moves(moves: str) -> list[tuple[int, int, int]]:
        """Convert a collection of box move descriptions into a usable
        list of move data.

        move 1 from 2 to 3 -> (1, 2, 3)
        move 4 from 5 to 6 -> (4, 5, 6)

        [(1, 2, 3), (4, 5, 6)]
        """
        rows = moves.split('\n')

        move_list = list()
        for row in rows:
            # Makes ['move', '<amount>', 'from', '<from_stack>', 'to', '<to_stack>']
            split = row.split(' ')
            move_list.append((int(split[1]), int(split[3]), int(split[5])))
        return move_list

    def step_1(self) -> str:
        # Process input data
        layout, moves = self.input.split('\n\n')
        stack = self.process_stack(layout)
        move_list = self.process_moves(moves)

        # Process moves sequentially
        for move in move_list:
            amount, from_, to = move
            # Moves happen one by one "amount" number of times.
            for i in range(amount):
                # Take the top box off the "from" stack with `.pop()` and add to "to" stack with `.append()`
                stack[to].append(stack[from_].pop())

        # Join the top box from each stack into a single string
        return ''.join([c[-1] for c in stack.values()])

    def step_2(self) -> str:
        # Process input data
        layout, moves = self.input.split('\n\n')
        stack = self.process_stack(layout)
        move_list = self.process_moves(moves)

        # Process moves sequentially
        for move in move_list:
            amount, from_, to = move

            # Select top "amount" of boxes from the "from" stack and put them on the "to" stack
            stack[to] += stack[from_][-amount:]
            # Remove the top "amount" of boxes from the "from" stack
            del stack[from_][-amount:]

        # Join the top box from each stack into a single string
        return ''.join([c[-1] for c in stack.values()])

    def run(self) -> None:
        self.header()
        print(f'Step 1: {self.step_1()}')
        print(f'Step 2: {self.step_2()}')


if __name__ == "__main__":
    Day5().run()
