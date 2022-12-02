import requests
import abc
import os


class AdventOfCode2022Day(abc.ABC):
    """The abstract parent class for any Advent of Code days."""

    def __init_subclass__(cls, day: int = None, **kwargs):
        """Takes a subclass argument indicating what day the code is for.

        This day is later used to pull the correct day's input.
        """

        if not day:
            raise ValueError('Missing subclass argument "day".')
        cls.day = day

    def __init__(self) -> None:
        """Gets the input from the AoC website when the class is instantiated."""
        self.input = self._get_input().strip()

    def _get_input(self):
        """Get the input from the AoC website using the session key configured
        in the environment variables and the current day.
        """

        r = requests.get(
            f'https://adventofcode.com/2022/day/{self.day}/input',
            cookies={'session': os.getenv('SESSION_KEY')}
        )
        r.raise_for_status()
        return r.text

    def header(self) -> None:
        """Prints a simple headers for the given day."""
        header = f'Advent of Code 2022 Day {self.day}'
        print('-' * len(header), header, '-' * len(header), sep='\n')

    @abc.abstractmethod
    def run(self) -> None:
        """Intended for implementation in the child class, actually runs the process for a given day."""
        pass

