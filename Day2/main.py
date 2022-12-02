from enum import Enum


class Move(Enum):
    """Enum for representing an individual move.

    The enum accepts multiple values, the first being the number of points the move is worth,
    and the other two being the possible values that represent that move.
    """
    Rock = 1, "A", "X"
    Paper = 2, "B", "Y"
    Scissors = 3, "C", "Z"

    def __new__(cls, *values):
        """Updates the __new__ class creator to allow multiple values for an enum field."""
        obj = object.__new__(cls)

        # Set the primary value to the first value.
        obj._value_ = values[0]

        # Allow other values to be mapped as well.
        for other_value in values[1:]:
            cls._value2member_map_[other_value] = obj

        obj._all_values = values
        return obj

    def __gt__(self, other: 'Move') -> bool:
        """Compares a move to the current move to see if the other move.

        A move is greater than another move if it wins against that move.
        """

        if not isinstance(other, Move):
            raise ValueError(f'Cannot compare a Move to a {other}.')

        # Check if the current move is the winner against the other move.
        return self == other.get_winner()

    def get_winner(self) -> 'Move':
        """Get the move that wins against the current move."""
        if self == Move.Rock:
            return Move.Paper
        elif self == Move.Paper:
            return Move.Scissors
        elif self == Move.Scissors:
            return Move.Rock

    def get_loser(self) -> 'Move':
        """Get the move that loses against the current move."""
        if self == Move.Rock:
            return Move.Scissors
        elif self == Move.Paper:
            return Move.Rock
        elif self == Move.Scissors:
            return Move.Paper

    def get_recommended_move(self, recommended: str) -> 'Move':
        """Get the move that is being recommended."""

        # End in a draw
        if recommended == "Y":
            return self
        # Need to lose
        elif recommended == "X":
            return self.get_loser()
        # Need to win
        elif recommended == "Z":
            return self.get_winner()

        raise ValueError(f'Recommended move type not handled: {recommended}.')


def get_input() -> str:
    """Read data input from file."""
    with open('./input.txt', 'r') as f:
        return f.read()


def get_points_for_round(opponent_move: Move, player_move: Move) -> int:
    """Get points from Move enum value.

    Draw = 3 pts
    Win  = 6 pts
    Loss = 0 pts
    """
    points: int = player_move.value

    # Draw
    if player_move == opponent_move:
        points += 3

    # Win
    if player_move > opponent_move:
        points += 6

    return points


def step_1(data: str) -> int:
    """Read the first value in the round as the opponent move, and the second value as the player move."""

    points = 0
    for round in data.split('\n'):
        opponent_move, player_move = round.split(' ')

        # Read the moves as enums
        opponent_move = Move(opponent_move)
        player_move = Move(player_move)

        # Get the number of points for the round
        points += get_points_for_round(opponent_move, player_move)
    return points


def step_2(data: str) -> int:
    """Read the first value in a round as the opponent move,
    and the second value as the response the player should take.

    X = Lose
    Y = Draw
    Z = Win
    """

    points = 0
    for round in data.split('\n'):
        opponent_move, player_move = round.split(' ')
        opponent_move = Move(opponent_move)
        player_move = opponent_move.get_recommended_move(player_move)
        points += get_points_for_round(opponent_move, player_move)
    return points


if __name__ == "__main__":
    print('Advent of Code 2022 Day 2', '-------------------------', sep='\n')
    data = get_input()
    print(f'Step 1: {step_1(data)}')
    print(f'Step 2: {step_2(data)}')
