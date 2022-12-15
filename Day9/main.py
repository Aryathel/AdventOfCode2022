from enum import Enum

from utils import AdventOfCode2022Day


class MoveDir(Enum):
    Left = "L"
    Right = "R"
    Up = "U"
    Down = "D"


class Move:
    def __init__(self, inp: str) -> None:
        move_dir, amount = inp.split(' ')
        self.move_dir = MoveDir(move_dir)
        self.amount = int(amount)

    def __str__(self) -> str:
        return f'<Move move_dir={self.move_dir} amount={self.amount}>'


class Day9(AdventOfCode2022Day, day=9):
    def get_moves(self) -> list[Move]:
        return [Move(m) for m in self.input.strip().split('\n')]

    def move_tail(self, head: list[int, int], tail: list[int, int], move: Move) -> list[int, int]:
        move_tail = False
        # Check if the tail needs to move horizontally
        if abs(head[0] - tail[0]) > 1 and head[1] == tail[1]:
            move_tail = True
        # Check if the tail needs to move vertically
        elif abs(head[1] - tail[1]) > 1 and head[0] == tail[0]:
            move_tail = True
        # Check if the tail needs to move diagonally
        elif abs(head[1] - tail[1]) + abs(head[0] - tail[0]) > 2:
            move_tail = True

        # Move the tail to be right behind the head depending on the move direction.
        if move_tail:
            tail = head.copy()
            if move.move_dir == MoveDir.Right:
                tail[0] -= 1
            elif move.move_dir == MoveDir.Left:
                tail[0] += 1
            elif move.move_dir == MoveDir.Up:
                tail[1] -= 1
            elif move.move_dir == MoveDir.Down:
                tail[1] += 1

        return tail

    def move(
            self,
            head: list[int, int],
            tail: list[int, int],
            move: Move,
            tail_positions: list[list[int, int]]
    ) -> tuple[
        list[int, int],
        list[int, int],
        list[list[int, int]]
    ]:
        # Setting up the looping params
        index = -1
        mod = 0
        if move.move_dir == MoveDir.Up:
            index = 1
            mod = 1
        elif move.move_dir == MoveDir.Right:
            index = 0
            mod = 1
        elif move.move_dir == MoveDir.Down:
            index = 1
            mod = -1
        elif move.move_dir == MoveDir.Left:
            index = 0
            mod = -1

        # Make the moves sequentially
        for i in range(move.amount):
            head[index] += mod
            tail = self.move_tail(head, tail, move)
            # Add any unique tail positions to the list
            if tail not in tail_positions:
                tail_positions.append(tail)

        return head, tail, tail_positions

    def move_rope(
            self,
            rope: list[list[int, int]],
            move: Move,
            tail_positions: list[list[int, int]]
    ) -> tuple[
        list[list[int, int]],
        list[list[int, int]]
    ]:
        # Setting up the looping params
        index = -1
        mod = 0
        if move.move_dir == MoveDir.Up:
            index = 1
            mod = 1
        elif move.move_dir == MoveDir.Right:
            index = 0
            mod = 1
        elif move.move_dir == MoveDir.Down:
            index = 1
            mod = -1
        elif move.move_dir == MoveDir.Left:
            index = 0
            mod = -1

        # Make the moves sequentially
        for _ in range(move.amount):
            rope[0][index] += mod
            for i in range(1, len(rope)):
                rope[i] = self.move_tail(rope[i-1], rope[i], move)
            # Add any unique tail positions to the list
            if rope[-1] not in tail_positions:
                tail_positions.append(rope[-1])

        return rope, tail_positions

    def step_1(self) -> int:
        moves = self.get_moves()

        tail_positions = [[0, 0]]

        head = [0, 0]
        tail = [0, 0]

        for move in moves:
            head, tail, tail_positions = self.move(head, tail, move, tail_positions)

        return len(tail_positions)

    def step_2(self) -> int:
        moves = self.get_moves()

        tail_positions = [[0, 0]]

        rope = []
        for i in range(9):
            rope.append([0, 0])

        for move in moves:
            rope, tail_positions = self.move_rope(rope, move, tail_positions)

        return len(tail_positions)

    def run(self) -> None:
        self.header()
        print(f'Step 1: {self.step_1()}')
        print(f'Step 2: {self.step_2()}')


if __name__ == "__main__":
    Day9().run()
