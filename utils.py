import requests
import abc
import os


class AdventOfCode2022:
    def __init__(self, session_key: str) -> None:
        self.session_key = session_key

    def get_input(self, day: int) -> str:
        r = requests.get(
            f'https://adventofcode.com/2022/day/{day}/input',
            cookies={'session': self.session_key}
        )
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            print(r.text)
            raise e
        return r.text


class AdventOfCode2022Day(abc.ABC):
    def __init_subclass__(cls, day: int = None, **kwargs):
        if not day:
            raise ValueError('Missing subclass argument "day".')
        cls.day = day
        cls._aoc = AdventOfCode2022(os.getenv('SESSION_KEY'))

    def __init__(self) -> None:
        self.input = self._get_input().strip()

    def _get_input(self):
        return self._aoc.get_input(self.day)

    def header(self) -> None:
        header = f'Advent of Code 2022 Day {self.day}'
        print('-' * len(header), header, '-' * len(header), sep='\n')

    @abc.abstractmethod
    def run(self) -> None:
        pass

